"""
Visualize OCR accuracy results
Creates charts and graphs for accuracy metrics
"""
import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend


def load_accuracy_report():
    """Load accuracy report from JSON"""
    report_path = Path(__file__).parent / 'results' / 'accuracy_report.json'
    
    if not report_path.exists():
        print(f"❌ Accuracy report not found: {report_path}")
        print("   Please run calculate_accuracy.py first!")
        return None
    
    with open(report_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_accuracy_chart(data, output_dir):
    """Create bar chart comparing accuracy metrics"""
    if 'details' not in data:
        return
    
    # Filter successful evaluations
    successful = [d for d in data['details'] if 'error' not in d]
    
    if not successful:
        print("⚠️  No successful evaluations to visualize")
        return
    
    doc_ids = [d['doc_id'].replace('dl_2025_', '') for d in successful]
    char_acc = [d['char_accuracy'] for d in successful]
    word_acc = [d['word_accuracy'] for d in successful]
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Chart 1: Character vs Word Accuracy
    x = np.arange(len(doc_ids))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, char_acc, width, label='Character Accuracy', color='#4CAF50')
    bars2 = ax1.bar(x + width/2, word_acc, width, label='Word Accuracy', color='#2196F3')
    
    ax1.set_xlabel('Document', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
    ax1.set_title('OCR Accuracy Comparison\n(Character vs Word Level)', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(doc_ids)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim([0, 105])
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=9)
    
    # Chart 2: Error Rates (CER vs WER)
    cer_values = [d['cer'] * 100 for d in successful]  # Convert to percentage
    wer_values = [d['wer'] * 100 for d in successful]
    
    bars3 = ax2.bar(x - width/2, cer_values, width, label='CER', color='#FF9800')
    bars4 = ax2.bar(x + width/2, wer_values, width, label='WER', color='#F44336')
    
    ax2.set_xlabel('Document', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Error Rate (%)', fontsize=12, fontweight='bold')
    ax2.set_title('OCR Error Rates\n(CER vs WER)', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(doc_ids)
    ax2.legend()
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bars in [bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    # Save
    output_path = output_dir / 'accuracy_chart.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Accuracy chart saved: {output_path}")


def create_metrics_summary(data, output_dir):
    """Create summary visualization with key metrics"""
    if 'average_char_accuracy' not in data:
        return
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # Overall metrics
    avg_char_acc = data['average_char_accuracy']
    avg_word_acc = data['average_word_accuracy']
    avg_cer = data['average_cer'] * 100
    avg_wer = data['average_wer'] * 100
    
    # 1. Average Accuracy Gauge
    categories = ['Character\nAccuracy', 'Word\nAccuracy']
    values = [avg_char_acc, avg_word_acc]
    colors = ['#4CAF50', '#2196F3']
    
    bars = ax1.barh(categories, values, color=colors)
    ax1.set_xlabel('Accuracy (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Average OCR Accuracy', fontsize=14, fontweight='bold')
    ax1.set_xlim([0, 100])
    ax1.grid(axis='x', alpha=0.3)
    
    for i, (bar, val) in enumerate(zip(bars, values)):
        ax1.text(val + 1, i, f'{val:.2f}%', va='center', fontweight='bold')
    
    # 2. Average Error Rates
    error_categories = ['CER', 'WER']
    error_values = [avg_cer, avg_wer]
    error_colors = ['#FF9800', '#F44336']
    
    bars2 = ax2.barh(error_categories, error_values, color=error_colors)
    ax2.set_xlabel('Error Rate (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Average Error Rates', fontsize=14, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    
    for i, (bar, val) in enumerate(zip(bars2, error_values)):
        ax2.text(val + 0.5, i, f'{val:.2f}%', va='center', fontweight='bold')
    
    # 3. Document Coverage
    successful = [d for d in data['details'] if 'error' not in d]
    doc_ids = [d['doc_id'].replace('dl_2025_', '') for d in successful]
    char_counts = [d['char_count_gt'] for d in successful]
    
    ax3.bar(doc_ids, char_counts, color='#9C27B0')
    ax3.set_xlabel('Document', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Character Count', fontsize=12, fontweight='bold')
    ax3.set_title('Ground Truth Document Sizes', fontsize=14, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    
    for i, (doc, count) in enumerate(zip(doc_ids, char_counts)):
        ax3.text(i, count, f'{count}', ha='center', va='bottom', fontsize=9)
    
    # 4. Summary Statistics Table
    ax4.axis('off')
    
    summary_data = [
        ['Metric', 'Value'],
        ['Total Documents Evaluated', f"{data['successful_evaluations']}/{data['total_documents']}"],
        ['Average Character Accuracy', f"{avg_char_acc:.2f}%"],
        ['Average Word Accuracy', f"{avg_word_acc:.2f}%"],
        ['Average CER', f"{avg_cer:.2f}%"],
        ['Average WER', f"{avg_wer:.2f}%"],
    ]
    
    table = ax4.table(cellText=summary_data, cellLoc='left',
                     bbox=[0, 0.2, 1, 0.6],
                     colWidths=[0.6, 0.4])
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)
    
    # Style header row
    for i in range(2):
        table[(0, i)].set_facecolor('#3F51B5')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(summary_data)):
        for j in range(2):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#E8EAF6')
    
    ax4.set_title('Summary Statistics', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save
    output_path = output_dir / 'performance_metrics.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Performance metrics saved: {output_path}")


def main():
    """Main visualization function"""
    print("=" * 80)
    print("OCR ACCURACY VISUALIZATION")
    print("=" * 80)
    print()
    
    # Load data
    data = load_accuracy_report()
    
    if not data:
        return
    
    # Create output directory
    output_dir = Path(__file__).parent / 'results'
    output_dir.mkdir(exist_ok=True)
    
    # Generate visualizations
    print("📊 Creating accuracy comparison chart...")
    create_accuracy_chart(data, output_dir)
    
    print("📊 Creating performance metrics summary...")
    create_metrics_summary(data, output_dir)
    
    print()
    print("=" * 80)
    print("✅ All visualizations created successfully!")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print("=" * 80)


if __name__ == '__main__':
    main()
