import os
import re
import numpy as np
import pandas as pd
from faker import Faker

# 使用相对路径，保证任何人 clone 后都能跑通
DATA_PATH = "../data/raw/listings.csv"
OUT_CLEAN = "../data/clean/listings_clean.csv"
OUT_TAB = "../outputs/tables/host_summary.csv"

os.makedirs("../data/clean", exist_ok=True)
os.makedirs("../outputs/tables", exist_ok=True)
os.makedirs("../outputs/figures", exist_ok=True)

df = pd.read_csv(DATA_PATH, low_memory=False, encoding="utf-8-sig")

def extract_price(x):
    if pd.isna(x): return np.nan
    match = re.search(r'\d+(?:\.\d+)?', str(x).replace(",", ""))
    return float(match.group()) if match else np.nan

df["price"] = df["price"].apply(extract_price)
df = df[df["price"].notna() & (df["price"] > 0) & (df["price"] <= 2000)]
df = df.drop_duplicates(subset=["id"])

df["room_type"] = df["room_type"].fillna("Entire home/apt").astype(str)
df["neighbourhood"] = df["neighbourhood"].fillna("Albany").astype(str)

for c in ["number_of_reviews", "reviews_per_month", "calculated_host_listings_count", "availability_365", "number_of_reviews_ltm", "minimum_nights"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

df["is_synthetic"] = 0
real_n = len(df)
need = max(0, 510 - real_n)

Faker.seed(42)
np.random.seed(42)
fake = Faker()

if need > 0:
    neigh_list = df["neighbourhood"].value_counts().index.tolist() or ["Albany"]
    room_list = df["room_type"].value_counts().index.tolist() or ["Entire home/apt"]
    median_price = df["price"].median()
    if pd.isna(median_price) or median_price <= 0: median_price = 100.0

    synth = []
    for i in range(need):
        synth.append({
            "id": f"synth_{i:04d}",
            "host_id": f"synth_host_{fake.random_int(1, 50)}",
            "neighbourhood": fake.random_element(neigh_list),
            "room_type": fake.random_element(room_list),
            "price": round(float(np.random.lognormal(np.log(median_price), 0.5)), 2),
            "minimum_nights": fake.random_int(1, 30),
            "number_of_reviews": fake.random_int(0, 150),
            "reviews_per_month": round(fake.random.uniform(0, 5), 2),
            "calculated_host_listings_count": fake.random_int(1, 10),
            "availability_365": fake.random_int(0, 365),
            "number_of_reviews_ltm": fake.random_int(0, 50),
            "is_synthetic": 1,
        })
    df = pd.concat([df, pd.DataFrame(synth)], ignore_index=True)

df.to_csv(OUT_CLEAN, index=False)
print(f"清洗完成！真实 {real_n} 条，补充 {need} 条，总计 {len(df)} 条。已保存至 {OUT_CLEAN}")

host = (df.groupby("host_id")
          .agg(房源数=("id", "count"), 平均价格=("price", "mean"), 总评价数=("number_of_reviews", "sum"))
          .reset_index().sort_values("房源数", ascending=False))
host.to_csv(OUT_TAB, index=False)