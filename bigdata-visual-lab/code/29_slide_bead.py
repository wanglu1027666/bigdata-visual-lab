import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=13, header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist()
y = np.arange(len(labels)); fig, ax = plt.subplots(figsize=(9,5))
ax.hlines(y, 0, 1, color="#D9D9D9", lw=8); ax.scatter(vals, y, s=200, color="#4472C4", zorder=3)
for i, v in zip(y, vals): ax.text(v, i+0.25, f"{float(v):.0%}", ha="center")
ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_xlim(0, 1.05); ax.set_title("滑珠图")
fig.savefig(os.path.join(OUT, "29_slide_bead.png"), dpi=150); plt.close(fig)