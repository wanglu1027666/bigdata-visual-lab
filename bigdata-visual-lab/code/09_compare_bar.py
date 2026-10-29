import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="9 对比柱形图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v21 = df.iloc[2:, 2].dropna().tolist(); v22 = df.iloc[2:, 3].dropna().tolist()
x = np.arange(len(labels)); w = 0.35; fig, ax = plt.subplots(figsize=(9,5))
ax.bar(x-w/2, v21, w, label="2021", color="#4472C4"); ax.bar(x+w/2, v22, w, label="2022", color="#ED7D31")
ax.set_xticks(x); ax.set_xticklabels(labels); ax.legend(); ax.set_title("对比柱形图")
fig.savefig(os.path.join(OUT, "09_compare_bar.png"), dpi=150); plt.close(fig)