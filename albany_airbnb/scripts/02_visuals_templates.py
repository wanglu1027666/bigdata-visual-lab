import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
import numpy as np
import os

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"

df = pd.read_csv("../data/clean/listings_clean.csv")
OUT = "../outputs/figures/"

# fig01
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df["price"], bins=50, color="#2E5C8A", edgecolor="white")
ax.set_title("房源价格分布直方图"); ax.set_xlabel("价格（美元/晚）"); ax.set_ylabel("房源数（条）")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout(); plt.savefig(OUT + "fig01_price_hist.png"); plt.close()

# fig02
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="room_type", y="price", ax=ax, palette="Set2")
ax.set_title("不同房型的价格分布箱线图"); ax.set_xlabel("房型"); ax.set_ylabel("价格（美元/晚）")
plt.tight_layout(); plt.savefig(OUT + "fig02_roomtype_price_box.png"); plt.close()

# fig03
top10 = df["neighbourhood"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top10.index[::-1], top10.values[::-1], color="#2E5C8A")
for i, v in enumerate(top10.values[::-1]):
    ax.text(v + 0.5, i, str(v), va="center", fontsize=8)
ax.set_title("Top10 街区房源数"); ax.set_xlabel("房源数（条）"); ax.set_ylabel("街区")
plt.tight_layout(); plt.savefig(OUT + "fig03_neigh_count_bar.png"); plt.close()

# fig04
top10_neigh = df["neighbourhood"].value_counts().head(10).index
ct = pd.crosstab(df[df["neighbourhood"].isin(top10_neigh)]["neighbourhood"], df[df["neighbourhood"].isin(top10_neigh)]["room_type"])
fig, ax = plt.subplots(figsize=(12, 5))
ct.plot(kind="bar", stacked=True, ax=ax, colormap="Set2")
ax.set_title("Top10 街区房源房型结构（堆积柱形图）"); ax.set_xlabel("街区"); ax.set_ylabel("房源数（条）")
ax.legend(title="房型", loc="upper right"); plt.xticks(rotation=45, ha="right")
plt.tight_layout(); plt.savefig(OUT + "fig04_neigh_roomtype_stacked.png"); plt.close()

# fig05
fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(df["price"], df["number_of_reviews"], s=20, alpha=0.5, c="#2E5C8A", edgecolors="k", linewidths=0.3)
ax.set_title("价格与评价数散点图"); ax.set_xlabel("价格（美元/晚）"); ax.set_ylabel("评价数（条）")
plt.tight_layout(); plt.savefig(OUT + "fig05_price_reviews_scatter.png"); plt.close()

# fig06
fig, ax = plt.subplots(figsize=(9, 6))
sc = ax.scatter(df["price"], df["number_of_reviews"], s=df["calculated_host_listings_count"] * 10 + 10, c=df["availability_365"], cmap="viridis", alpha=0.6, edgecolors="k", linewidths=0.3)
ax.set_title("价格—评价数气泡图"); ax.set_xlabel("价格（美元/晚）"); ax.set_ylabel("评价数（条）")
cbar = plt.colorbar(sc, ax=ax); cbar.set_label("可租天数（天）")
plt.tight_layout(); plt.savefig(OUT + "fig06_bubble.png"); plt.close()

# fig07
sub = df[df["neighbourhood"].isin(top10_neigh)]
ct = pd.crosstab(sub["neighbourhood"], sub["room_type"])
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(ct, annot=True, fmt="d", cmap="YlOrRd", ax=ax, cbar_kws={"label": "房源数（条）"})
ax.set_title("Top10 街区×房型房源数热力图"); ax.set_xlabel("房型"); ax.set_ylabel("街区")
plt.tight_layout(); plt.savefig(OUT + "fig07_heatmap.png"); plt.close()

# fig08
room_counts = df["room_type"].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(room_counts.values, labels=room_counts.index, autopct="%1.1f%%", colors=sns.color_palette("Set2"), startangle=90, wedgeprops={"edgecolor": "white"})
ax.set_title("房源房型占比")
plt.tight_layout(); plt.savefig(OUT + "fig08_roomtype_pie.png"); plt.close()

# fig09
host_counts = df.groupby("host_id")["id"].count().sort_values(ascending=False).values
cum = np.cumsum(host_counts) / host_counts.sum()
fig, ax = plt.subplots(figsize=(10, 4))
ax.fill_between(range(len(cum)), cum, color="#2E5C8A", alpha=0.5)
ax.plot(range(len(cum)), cum, color="#2E5C8A", linewidth=1.5)
ax.set_title("房东房源累计占比面积图"); ax.set_xlabel("房东数（按房源数降序）"); ax.set_ylabel("累计房源占比"); ax.set_ylim(0, 1.05)
plt.tight_layout(); plt.savefig(OUT + "fig09_cum_area.png"); plt.close()

# fig10
neigh_agg = (df.groupby("neighbourhood").agg(房源数=("id", "count"), 平均价格=("price", "mean"), 平均评价数=("number_of_reviews", "mean")).sort_values("房源数", ascending=False).head(5))
norm = (neigh_agg - neigh_agg.min()) / (neigh_agg.max() - neigh_agg.min() + 1e-9)
labels = list(norm.columns); n = len(labels); angles = [i / n * 2 * pi for i in range(n)]; angles += angles[:1]
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
colors = sns.color_palette("Set2", len(norm))
for (name, row), c in zip(norm.iterrows(), colors):
    values = row.tolist() + [row.tolist()[0]]
    ax.plot(angles, values, color=c, linewidth=1.5, label=name)
    ax.fill(angles, values, color=c, alpha=0.1)
ax.set_xticks(angles[:-1]); ax.set_xticklabels(labels)
ax.set_title("Top5 街区特征雷达图"); ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
plt.tight_layout(); plt.savefig(OUT + "fig10_radar.png"); plt.close()

print("fig01–fig10 模板图已生成完毕！")