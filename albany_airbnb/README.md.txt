# 奥尔巴尼 Airbnb 房源分群与定价分析

## 1. 项目简介
基于 Inside Airbnb Albany 快照，完成数据获取→清洗→帕累托/K-Means/Apriori→可视化→Streamlit 大屏的端到端商业分析。

## 2. 数据来源与合规声明
- 数据源：Inside Airbnb (https://insideairbnb.com/get-the-data/)
- 获取方式：官方页面手动下载 CSV（白名单），未使用爬虫
- 获取日期：2026-11-03
- 数据规模：真实 462 条 + Faker 补充 48 条 = 510 条（`is_synthetic` 标注）

## 3. 目录结构
```text
albany_airbnb/
├── data/
│   ├── raw/                 # 原始数据 (listings.csv)
│   └── clean/               # 清洗后数据 (listings_clean.csv)
├── scripts/
│   ├── 01_clean.py          # 数据清洗与补充
│   ├── 02_visuals_templates.py # 10 张模板图
│   ├── 03_models_business.py   # 6 张业务图
│   └── 04_dashboard.py      # Streamlit 交互大屏
├── outputs/
│   ├── figures/             # 生成的 16 张图
│   └── tables/              # 结果汇总表
├── docs/                    # 期末大论文
├── run_all.py               # 一键复现脚本
├── requirements.txt         # 依赖清单
└── README.md