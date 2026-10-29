import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=12, header=None).dropna(subset=[1])
labels = df.iloc[2:, 1].tolist(); vals = df.iloc[2:, 2].tolist(); q_vals = df.iloc[2:, 3].tolist()
fig, ax = plt.subplots(figsize=(12,5)); ax.bar(labels, vals, color="#5B9BD5", label="月度")
ax2 = ax.twinx(); ax2.plot(labels, q_vals, color="#ED7D31", marker="o", label="季度累计")
ax.legend(loc="upper left"); ax2.legend(loc="upper right"); ax.set_title("复合柱形图")
fig.savefig(os.path.join(OUT, "28_composite_bar.png"), dpi=150); plt.close(fig)