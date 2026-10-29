import pandas as pd, os
from pyecharts.charts import Liquid
from pyecharts import options as opts
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(前15).xlsx"), sheet_name="15 水球图", header=None)
val = float(df.iloc[2, 1])
c = Liquid().add("完成率", [val], is_outline_show=False).set_global_opts(title_opts=opts.TitleOpts(title="水球图"))
c.render(os.path.join(OUT, "15_liquid.html"))