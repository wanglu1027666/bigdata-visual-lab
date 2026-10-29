import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="7 蝴蝶图", header=None)
labels = df.iloc[2:, 1].dropna().tolist(); v1 = df.iloc[2:, 2].dropna().tolist(); v2 = df.iloc[2:, 3].dropna().tolist()
fig, ax = plt.subplots(figsize=(10,5)); ax.axis("off")
for i in range(len(labels)):
    left = "|" * int(float(v1[i]) * 40); right = "|" * int(float(v2[i]) * 40); y_pos = 1 - i * 0.15
    ax.text(0.35, y_pos, left, ha="right", color="#4472C4", family="monospace"); ax.text(0.45, y_pos, f" {labels[i]} ", ha="center")
    ax.text(0.55, y_pos, right, ha="left", color="#ED7D31", family="monospace")
ax.set_title("REPT 蝴蝶图")
fig.savefig(os.path.join(OUT, "07_rept_butterfly.png"), dpi=150); plt.close(fig)