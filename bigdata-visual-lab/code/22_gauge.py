import pandas as pd, os
from pyecharts.charts import Gauge
from pyecharts import options as opts
BASE = r"C:\Users\茶叶蛋\Desktop\bigdata-visual-lab"; OUT = os.path.join(BASE, "outputs")
df = pd.read_excel(os.path.join(BASE, "data", "第二章 图表(后15).xlsx"), sheet_name=6, header=None)
val = float(df.iloc[2, 7])
g = Gauge().add("", [("完成率", val)], min_=50, max_=150, axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=[[0.3,"#FD6666"],[0.7,"#FFC107"],[1,"#67e0e3"]], width=20)))
g.set_global_opts(title_opts=opts.TitleOpts(title="仪表盘图")).render(os.path.join(OUT, "22_gauge.html"))