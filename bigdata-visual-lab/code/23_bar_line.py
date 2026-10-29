import pandas as pd, matplotlib.pyplot as plt, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=7, header=None)
years = df.iloc[2:, 1].dropna().astype(str).tolist(); vals = df.iloc[2:, 2].dropna().tolist(); ratios = df.iloc[2:, 3].dropna().tolist()
fig, ax1 = plt.subplots(figsize=(9,5)); ax1.bar(years, vals, color="#5B9BD5", label="销售量")
ax2 = ax1.twinx(); ax2.plot(years, [float(r)*100 for r in ratios], color="#ED7D31", marker="o", label="同比%")
ax1.set_title("柱形折线图"); fig.legend()
fig.savefig(os.path.join(OUT, "23_bar_line.png"), dpi=150); plt.close(fig)