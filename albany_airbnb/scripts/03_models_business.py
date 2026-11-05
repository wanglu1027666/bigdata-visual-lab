import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mlxtend.frequent_patterns import apriori, association_rules
import os

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"

df = pd.read_csv("../data/clean/listings_clean.csv")
OUT = "../outputs/figures/"

# fig11
host_counts = df.groupby("host_id")["id"].count().sort_values(ascending=False)
cum_ratio = host_counts.cumsum() / host_counts.sum()
n = len(host_counts); top20_idx = int(np.ceil(n * 0.2)); top20_share = cum_ratio.iloc[top20_idx - 1]
print(f"前 20% 房东持有房源占比 {top20_share:.2%}")

fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.bar(range(n), host_counts.values, color="#2E5C8A", width=0.8)
ax1.set_xlabel("房东（按房源数降序）"); ax1.set_ylabel("房源数（条）", color="#2E5C8A"); ax1.tick_params(axis="y", labelcolor="#2E5C8A")
ax2 = ax1.twinx()
ax2.plot(range(n), cum_ratio.values, color="#C0504D", linewidth=2)
ax2.axhline(0.8, color="gray", linestyle="--", linewidth=1); ax2.axvline(top20_idx - 1, color="gray", linestyle="--", linewidth=1)
ax2.set_ylabel("累计占比", color="#C0504D"); ax2.tick_params(axis="y", labelcolor="#C0504D"); ax2.set_ylim(0, 1.05)
ax1.set_title(f"房东房源帕累托图（前20%房东持有{top20_share:.1%}房源）")
plt.tight_layout(); plt.savefig(OUT + "fig11_pareto.png"); plt.close()

# fig12 & fig13
feat_cols = ["price", "minimum_nights", "availability_365", "number_of_reviews"]
X = StandardScaler().fit_transform(df[feat_cols].fillna(df[feat_cols].median()))

K_range = range(2, 8); inertia, sil = [], []
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
    inertia.append(km.inertia_); sil.append(silhouette_score(X, km.labels_))
best_k = 5
df["cluster"] = KMeans(n_clusters=best_k, random_state=42, n_init=10).fit_predict(X)

fig, ax = plt.subplots(figsize=(9, 6))
sc = ax.scatter(df["price"], df["availability_365"], c=df["cluster"], cmap="viridis", s=40, alpha=0.6, edgecolors="k")
ax.set_title(f"房源 K-Means 聚类（k={best_k}）"); ax.set_xlabel("价格（美元/晚）"); ax.set_ylabel("可租天数（天）")
cbar = plt.colorbar(sc, ax=ax); cbar.set_label("簇")
plt.tight_layout(); plt.savefig(OUT + "fig12_cluster.png"); plt.close()

fig, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(list(K_range), inertia, "o-", color="#2E5C8A", label="SSE"); ax1.set_xlabel("k（簇数）"); ax1.set_ylabel("SSE", color="#2E5C8A"); ax1.tick_params(axis="y", labelcolor="#2E5C8A")
ax2 = ax1.twinx()
ax2.plot(list(K_range), sil, "s--", color="#C0504D", label="轮廓系数"); ax2.set_ylabel("轮廓系数", color="#C0504D"); ax2.tick_params(axis="y", labelcolor="#C0504D")
ax1.set_title("K-Means 参数选择：SSE 与轮廓系数")
plt.tight_layout(); plt.savefig(OUT + "fig13_k_selection.png"); plt.close()

# fig14 & fig15
basket = pd.DataFrame(index=df.index)
basket["房型_整套"] = df["room_type"] == "Entire home/apt"
basket["房型_单间"] = df["room_type"] == "Private room"
basket["价格_高"] = df["price"] > df["price"].median()
basket["价格_低"] = df["price"] <= df["price"].median()
basket["租期_长"] = df["minimum_nights"] >= 30
basket["可租_高频"] = df["availability_365"] >= 180
basket["评价_高"] = df["number_of_reviews"] > 50
basket = basket.astype(bool)

freq = pd.DataFrame()
for sup in [0.05, 0.03, 0.02, 0.01]:
    freq = apriori(basket, min_support=sup, use_colnames=True, max_len=4)
    if len(freq) > 0: break

rules = association_rules(freq, metric="lift", min_threshold=1.0).sort_values("lift", ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(rules["support"], rules["confidence"], c=rules["lift"], cmap="YlOrRd", s=60, edgecolors="k", alpha=0.7)
ax.set_title("关联规则散点图（颜色=提升度 Lift）"); ax.set_xlabel("支持度 Support"); ax.set_ylabel("置信度 Confidence")
cbar = plt.colorbar(sc, ax=ax); cbar.set_label("Lift")
plt.tight_layout(); plt.savefig(OUT + "fig14_rules_scatter.png"); plt.close()

high_rules = rules[rules["consequents"].apply(lambda x: "评价_高" in x)].head(10).copy()
fig, ax = plt.subplots(figsize=(12, 6))
labels = [" & ".join(list(r["antecedents"])) for _, r in high_rules.iterrows()]
ax.barh(range(len(high_rules)), high_rules["lift"], color="#2E5C8A")
ax.set_yticks(range(len(high_rules))); ax.set_yticklabels(labels, fontsize=8); ax.invert_yaxis()
ax.set_title("提升“高评价”概率的 Top10 关联规则"); ax.set_xlabel("提升度 Lift")
for i, v in enumerate(high_rules["lift"]):
    ax.text(v + 0.01, i, f"{v:.2f}", va="center", fontsize=8)
plt.tight_layout(); plt.savefig(OUT + "fig15_rules_lift_bar.png"); plt.close()

# fig16
profile = df.groupby("cluster").agg(平均价格=("price", "mean"), 平均可租天数=("availability_365", "mean"), 平均评价数=("number_of_reviews", "mean")).round(2)
fig, ax = plt.subplots(figsize=(10, 5))
profile.T.plot(kind="bar", ax=ax, colormap="Set2")
ax.set_title("各簇房源特征均值对比"); ax.set_xlabel("特征"); ax.set_ylabel("均值（原始单位）"); ax.legend(title="簇", loc="upper right")
plt.xticks(rotation=0)
plt.tight_layout(); plt.savefig(OUT + "fig16_cluster_profile.png"); plt.close()

# 这一步很重要：把聚类标签重新存回 CSV，供大屏调用
df.to_csv("../data/clean/listings_clean.csv", index=False)
print("fig11–fig16 业务模型图已生成，且聚类标签已保存至 CSV！")