import pandas as pd, matplotlib.pyplot as plt, numpy as np, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="6 蝴蝶图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v22 = df.iloc[2:, 3].dropna().tolist(); v21 = df.iloc[2:, 5].dropna().tolist()
y = np.arange(len(labels)); fig, ax = plt.subplots(figsize=(9,5))
ax.barh(y, [-v for v in v22], color="#4472C4", label="2022"); ax.barh(y, v21, color="#ED7D31", label="2021")
ax.set_yticks(y); ax.set_yticklabels(labels); ax.axvline(0, color="black", lw=0.8); ax.set_xticklabels([abs(int(t)) for t in ax.get_xticks()])
ax.legend(); ax.set_title("蝴蝶图")
fig.savefig(os.path.join(OUT, "06_butterfly_bar.png"), dpi=150); plt.close(fig)