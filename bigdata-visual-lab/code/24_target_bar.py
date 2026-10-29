import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=8, header=None)
labels = df.iloc[3:, 1].dropna().tolist(); actual = df.iloc[3:, 2].dropna().tolist(); target = df.iloc[3:, 3].dropna().tolist()
x = np.arange(len(labels)); w = 0.35; fig, ax = plt.subplots(figsize=(9,5))
ax.bar(x-w/2, actual, w, label="实际", color="#5B9BD5"); ax.bar(x+w/2, target, w, label="目标", color="#ED7D31")
ax.set_xticks(x); ax.set_xticklabels(labels); ax.legend(); ax.set_title("目标柱形图")
fig.savefig(os.path.join(OUT, "24_target_bar.png"), dpi=150); plt.close(fig)