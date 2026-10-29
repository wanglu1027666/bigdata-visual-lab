import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=11, header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v22 = df.iloc[2:, 2].dropna().tolist(); v21 = df.iloc[2:, 3].dropna().tolist(); ratios = df.iloc[2:, 4].dropna().tolist()
x = np.arange(len(labels)); w = 0.35; fig, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(x-w/2, v22, w, label="2022", color="#4472C4"); ax1.bar(x+w/2, v21, w, label="2021", color="#ED7D31")
ax2 = ax1.twinx(); ax2.plot(x, [float(r)*100 for r in ratios], color="green", marker="o", label="同比%")
ax1.set_xticks(x); ax1.set_xticklabels(labels); ax1.set_title("簇状柱形折线图"); fig.legend()
fig.savefig(os.path.join(OUT, "27_clustered_bar_line.png"), dpi=150); plt.close(fig)