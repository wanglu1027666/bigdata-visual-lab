import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="14 单值圆环图", header=None)
v = float(df.iloc[2, 1])
fig, ax = plt.subplots(figsize=(6,6)); ax.pie([v, 1-v], colors=["#4472C4", "#D9D9D9"], startangle=90, counterclock=False, wedgeprops=dict(width=0.3))
ax.text(0, 0, f"{v:.0%}", ha="center", va="center", fontsize=28); ax.set_title("单值圆环图")
fig.savefig(os.path.join(OUT, "14_single_donut.png"), dpi=150); plt.close(fig)