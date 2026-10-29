import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="8 数值百分比", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist(); pcts = df.iloc[2:, 5].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); ax.barh(labels, vals, color="#5B9BD5")
for i, (v, p) in enumerate(zip(vals, pcts)): ax.text(v+50, i, f"{float(p)*100:+.1f}%", va="center", color="red" if float(p)<0 else "green")
ax.set_title("数值百分比条形图")
fig.savefig(os.path.join(OUT, "08_pct_bar.png"), dpi=150); plt.close(fig)