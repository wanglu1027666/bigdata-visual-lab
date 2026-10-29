import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=1, header=None)
labels = df.iloc[2:, 1].dropna().tolist(); vals = df.iloc[2:, 2].dropna().tolist()
fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(aspect="equal"))
for i, v in enumerate(vals): ax.bar(0, float(v)*4, width=0.25, bottom=i*0.3, color=plt.cm.Blues(0.3+i*0.12), edgecolor="white")
ax.axis("off"); ax.set_title("玉玦图")
fig.savefig(os.path.join(OUT, "17_jade_ring.png"), dpi=150); plt.close(fig)