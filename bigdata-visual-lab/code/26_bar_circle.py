import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=10, header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist(); ratios = df.iloc[2:, 4].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); ax.bar(labels, vals, color="#5B9BD5")
for i in range(len(labels)): ax.scatter(i, vals[i]+300, s=float(ratios[i])*3000, color="#ED7D31", alpha=0.7)
ax.set_title("柱形圆（圆点大小表示同比）")
fig.savefig(os.path.join(OUT, "26_bar_circle.png"), dpi=150); plt.close(fig)