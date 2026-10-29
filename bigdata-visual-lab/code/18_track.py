import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=2, header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); y = np.arange(len(labels)); ax.barh(y, vals, color="#5B9BD5", height=0.6)
for i, v in zip(y, vals): ax.text(v+5, i, str(v), va="center")
ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_title("跑道图")
fig.savefig(os.path.join(OUT, "18_track.png"), dpi=150); plt.close(fig)