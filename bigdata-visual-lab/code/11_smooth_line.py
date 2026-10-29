import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
from scipy.interpolate import make_interp_spline
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="11 平滑折线图", header=None)
labels = df.iloc[2:, 2].dropna().tolist(); vals = df.iloc[2:, 3].dropna().tolist()
x = np.arange(len(vals)); xs = np.linspace(0, len(vals)-1, 300); ys = make_interp_spline(x, vals, k=3)(xs)
fig, ax = plt.subplots(figsize=(10,5)); ax.plot(xs, ys, color="#4472C4", lw=2); ax.scatter(x, vals, color="#ED7D31", zorder=3)
ax.set_xticks(x); ax.set_xticklabels(labels); ax.set_title("平滑折线图")
fig.savefig(os.path.join(OUT, "11_smooth_line.png"), dpi=150); plt.close(fig)