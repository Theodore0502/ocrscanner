import re

def renumber_figures_tables(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    out_lines = []
    
    current_chapter = 1
    fig_counter = 1
    tab_counter = 1
    
    for line in lines:
        if line.startswith("CHƯƠNG "):
            match = re.search(r'CHƯƠNG (\d+)', line)
            if match:
                current_chapter = int(match.group(1))
                fig_counter = 1
                tab_counter = 1
            out_lines.append(line)
        elif line.startswith("Hình ") and ":" not in line.split(".")[0]:
            # It's a figure caption
            # Example: Hình 2.1. Biểu đồ...
            new_line = re.sub(r'^Hình \d+\.\d+\.', f'Hình {current_chapter}.{fig_counter}.', line)
            out_lines.append(new_line)
            fig_counter += 1
        elif line.startswith("Bảng ") and ":" not in line.split(".")[0] and len(line.split()) > 1:
            # Check if it's really a table caption
            if re.match(r'^Bảng \d+(\.\d+)*\.*', line):
                new_line = re.sub(r'^Bảng \d+(\.\d+)*\.', f'Bảng {current_chapter}.{tab_counter}.', line)
                out_lines.append(new_line)
                tab_counter += 1
            else:
                out_lines.append(line)
        else:
            out_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))

renumber_figures_tables(r"f:\-----OCR_Scanner\bao_cao\bao_cao_chuan\bao_cao_QTDA_PhanMem.md")
