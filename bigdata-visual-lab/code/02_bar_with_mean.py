import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="2 带均值柱形图", header=None)
labels, vals = df.iloc[2:, 1].dropna().tolist(), df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(8,5)); ax.bar(labels, vals, color="#5B9BD5")
ax.axhline(sum(vals)/len(vals), color="red", ls="--", lw=1.5, label="均值")
ax.legend(); ax.set_title("带均值柱形图")
fig.savefig(os.path.join(OUT, "02_bar_with_mean.png"), dpi=150); plt.close(fig)