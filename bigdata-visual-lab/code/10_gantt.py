import pandas as pd, matplotlib.pyplot as plt, matplotlib.dates as mdates, os
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="10 甘特图", header=None)
tasks = df.iloc[3:, 1].dropna().tolist(); starts = pd.to_datetime(df.iloc[3:, 2].dropna()); days = df.iloc[3:, 3].dropna().tolist(); progress = df.iloc[3:, 4].dropna().tolist()
fig, ax = plt.subplots(figsize=(10,5))
for i in range(len(tasks)):
    ax.barh(i, days[i], left=starts.iloc[i], color="#9DC3E6", height=0.6); ax.barh(i, days[i]*progress[i], left=starts.iloc[i], color="#1F4E79", height=0.6)
ax.set_yticks(range(len(tasks))); ax.set_yticklabels(tasks); ax.xaxis_date(); ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d")); ax.set_title("甘特图")
fig.savefig(os.path.join(OUT, "10_gantt.png"), dpi=150); plt.close(fig)