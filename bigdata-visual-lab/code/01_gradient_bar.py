import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.colors import LinearSegmentedColormap
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"
DATA1 = os.path.join(BASE, "data", "第二章 图表(前15).xlsx")
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True) 
df_raw = pd.read_excel(DATA1, sheet_name="1 渐变柱形图", header=None)
regions = df_raw.iloc[2:, 1].dropna().tolist() 
vals = df_raw.iloc[2:, 2].dropna().tolist()    
print(f"成功读取数据！\n区域: {regions}\n销量: {vals}")
fig, ax = plt.subplots(figsize=(8, 5))
cmap = LinearSegmentedColormap.from_list("g", ["#9DC3E6", "#1F4E79"])
for i, v in enumerate(vals):
    ax.imshow(np.linspace(0, 1, 256).reshape(-1, 1),
              extent=(i-0.4, i+0.4, 0, v), aspect="auto",
              cmap=cmap, origin="lower", zorder=2)
ax.set_xticks(range(len(regions)))
ax.set_xticklabels(regions)
ax.set_xlim(-0.6, len(regions) - 0.4)
ax.set_ylim(0, max(vals) * 1.1)
ax.set_title("渐变柱形图", fontsize=14)
save_path = os.path.join(OUT, "01_gradient_bar.png")
fig.tight_layout()
fig.savefig(save_path, dpi=150)
plt.close(fig)
print("=" * 50)
print(f"代码执行完毕！图片已经保存到：\n{save_path}")
print("=" * 50)