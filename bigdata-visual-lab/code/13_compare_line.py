import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="13 对比折线图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v21 = df.iloc[2:, 2].dropna().tolist(); v22 = df.iloc[2:, 3].dropna().tolist()
fig, ax = plt.subplots(figsize=(9,5)); ax.plot(labels, v21, marker="o", label="2021"); ax.plot(labels, v22, marker="s", label="2022")
ax.legend(); ax.set_title("对比折线图")
fig.savefig(os.path.join(OUT, "13_compare_line.png"), dpi=150); plt.close(fig)