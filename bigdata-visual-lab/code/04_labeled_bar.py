import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="4 标注柱形图", header=None)
labels, vals = df.iloc[2:, 1].dropna().tolist(), df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(10,5)); bars = ax.bar(labels, vals, color="#5B9BD5")
for b, v in zip(bars, vals): ax.text(b.get_x()+b.get_width()/2, v+100, f"{v}", ha="center")
ax.set_title("标注柱形图")
fig.savefig(os.path.join(OUT, "04_labeled_bar.png"), dpi=150); plt.close(fig)