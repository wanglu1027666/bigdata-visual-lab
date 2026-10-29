import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
from matplotlib.colors import LinearSegmentedColormap
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="3 渐变圆角柱形图", header=None)
labels, vals = df.iloc[2:, 1].dropna().tolist(), df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(8,5)); cmap = LinearSegmentedColormap.from_list("g", ["#9DC3E6", "#2E75B6"])
for i, v in enumerate(vals): ax.imshow(np.linspace(0,1,256).reshape(-1,1), extent=(i-0.35, i+0.35, 0, v), aspect="auto", cmap=cmap, origin="lower", zorder=1)
ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels); ax.set_ylim(0, max(vals)*1.1); ax.set_title("渐变圆角柱形图")
fig.savefig(os.path.join(OUT, "03_rounded_gradient_bar.png"), dpi=150); plt.close(fig)