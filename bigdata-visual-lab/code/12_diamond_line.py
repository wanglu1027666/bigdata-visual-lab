import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="12 菱形走势图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); ax.plot(labels, vals, marker="D", markersize=10, color="#4472C4", markerfacecolor="#ED7D31", lw=2)
ax.set_title("菱形走势图")
fig.savefig(os.path.join(OUT, "12_diamond_line.png"), dpi=150); plt.close(fig)