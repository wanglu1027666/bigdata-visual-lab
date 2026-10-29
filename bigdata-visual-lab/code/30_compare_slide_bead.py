import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=14, header=None)
labels = df.iloc[3:, 1].dropna().tolist(); v22 = df.iloc[3:, 2].dropna().tolist(); v21 = df.iloc[3:, 3].dropna().tolist()
y = np.arange(len(labels)); fig, ax = plt.subplots(figsize=(9,5))
ax.hlines(y, 0, 1, color="#D9D9D9", lw=8); ax.scatter(v22, y, s=200, color="#4472C4", label="2022", zorder=3); ax.scatter(v21, y, s=200, color="#ED7D31", label="2021", zorder=3)
ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_xlim(0, 1.05); ax.legend(); ax.set_title("对比滑珠图")
fig.savefig(os.path.join(OUT, "30_compare_slide_bead.png"), dpi=150); plt.close(fig)