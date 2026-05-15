import re

def update_toc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all headings: lines starting with Chapter X or X.Y
    headings = []
    lines = content.split('\n')
    in_toc = False
    new_lines = []
    
    # Let's extract the headings for TOC
    for line in lines:
        if line.startswith("CHƯƠNG") and ":" in line:
            headings.append(line.strip())
        elif re.match(r'^[123]\.\d+(\.\d+)*\.* ', line):
            headings.append(line.strip())

    # Build the new TOC
    toc = []
    for h in headings:
        # Indent according to level
        level = len(re.findall(r'\.', h.split(' ')[0]))
        indent = "   " * (level - 1) if level > 0 else ""
        if h.startswith("CHƯƠNG"):
            toc.append(h)
        else:
            toc.append(indent + h)
            
    # Also find figures
    figures = []
    for line in lines:
        if line.startswith("Hình ") and ":" not in line.split(".")[0]:
            figures.append(line.strip())
            
    # Also find tables
    tables = []
    for line in lines:
        if line.startswith("Bảng ") and ":" not in line.split(".")[0]:
            tables.append(line.strip())

    # Reconstruct the file
    out_lines = []
    state = "normal"
    for line in lines:
        if "MỤC LỤC" in line:
            state = "toc"
            out_lines.append(line)
            for t in toc:
                out_lines.append(t)
            out_lines.append("")
        elif "DANH MỤC HÌNH ẢNH" in line:
            state = "fig"
            out_lines.append(line)
            for f in figures:
                out_lines.append(f)
            out_lines.append("")
        elif "DANH MỤC BẢNG BIỂU" in line:
            state = "tab"
            out_lines.append(line)
            for tb in tables:
                out_lines.append(tb)
            out_lines.append("")
        elif state in ["toc", "fig", "tab"]:
            # skip old toc, fig, tab until we see empty line or next section
            if line.startswith("DANH MỤC") or line.startswith("LỜI CẢM ƠN") or line.startswith("LỜI NÓI ĐẦU"):
                state = "normal"
                out_lines.append(line)
        else:
            out_lines.append(line)
            
    # Clean up empty lines
    cleaned = []
    for i, line in enumerate(out_lines):
        if line.strip() == "" and i > 0 and out_lines[i-1].strip() == "":
            continue
        cleaned.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned))

update_toc(r"f:\-----OCR_Scanner\bao_cao\bao_cao_chuan\bao_cao_QTDA_PhanMem.md")
