import pandas as pd, os
from pyecharts.charts import Pie
from pyecharts import options as opts
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=3, header=None)
data = [(str(a), float(b)) for a, b in zip(df.iloc[2:, 1].dropna(), df.iloc[2:, 2].dropna())]
c = Pie().add("", data, rosetype="area", radius=["0%", "75%"]).set_global_opts(title_opts=opts.TitleOpts(title="南丁格尔圆饼图"))
c.render(os.path.join(OUT, "19_rose_pie.html"))