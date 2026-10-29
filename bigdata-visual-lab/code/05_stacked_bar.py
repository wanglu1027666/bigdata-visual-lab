import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="5 层叠柱形图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v1 = df.iloc[2:, 2].dropna().tolist(); v2 = df.iloc[2:, 3].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); ax.bar(labels, v1, color="#5B9BD5", label="销售额"); ax.bar(labels, v2, color="#ED7D31", label="利润额")
ax.legend(); ax.set_title("层叠柱形图")
fig.savefig(os.path.join(OUT, "05_stacked_bar.png"), dpi=150); plt.close(fig)