import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Albany Airbnb 商业分析大屏", layout="wide")
st.title("🏠 Albany Airbnb 房源数据商业分析大屏")

@st.cache_data
def load_data():
    # 相对路径指向清洗后的数据
    path = "../data/clean/listings_clean.csv"
    return pd.read_csv(path)

df = load_data()

st.sidebar.header("🔍 数据筛选联动")
room_types = df['room_type'].unique().tolist()
selected_rooms = st.sidebar.multiselect("选择房型", room_types, default=room_types)

min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider("价格区间 (美元/晚)", min_price, max_price, (min_price, max_price))

filtered_df = df[(df['room_type'].isin(selected_rooms)) & 
                 (df['price'] >= price_range[0]) & 
                 (df['price'] <= price_range[1])]

col1, col2, col3 = st.columns(3)
col1.metric("筛选后房源总数", f"{len(filtered_df)} 套")
col2.metric("平均价格", f"${filtered_df['price'].mean():.2f}")
multi_host = filtered_df[filtered_df['calculated_host_listings_count'] > 1].shape[0] / len(filtered_df) if len(filtered_df) > 0 else 0
col3.metric("多房源房东占比", f"{multi_host:.1%}")

st.markdown("---")
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📍 Top10 街区房源数")
    neigh_counts = filtered_df['neighbourhood'].value_counts().head(10).reset_index()
    neigh_counts.columns = ['街区', '房源数']
    fig_bar = px.bar(neigh_counts, x='房源数', y='街区', orientation='h', color='房源数', color_continuous_scale="Blues")
    fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_bar, use_container_width=True)

with row1_col2:
    st.subheader("🎯 价格 vs 可租天数 (聚类散点)")
    fig_scatter = px.scatter(filtered_df, x="price", y="availability_365", 
                             color="cluster", size="number_of_reviews",
                             hover_data=["neighbourhood", "room_type"],
                             labels={"price": "价格 (美元)", "availability_365": "可租天数", "cluster": "聚类簇"})
    st.plotly_chart(fig_scatter, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🏘️ 房型占比")
    room_counts = filtered_df['room_type'].value_counts().reset_index()
    room_counts.columns = ['房型', '数量']
    fig_pie = px.pie(room_counts, names='房型', values='数量', hole=0.4, color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_pie, use_container_width=True)

with row2_col2:
    st.subheader("💰 各房型价格分布")
    fig_box = px.box(filtered_df, x="room_type", y="price", color="room_type", 
                     labels={"room_type": "房型", "price": "价格 (美元)"})
    st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")
st.subheader("📋 房源明细数据表")
st.dataframe(filtered_df[['id', 'neighbourhood', 'room_type', 'price', 'minimum_nights', 'number_of_reviews']].head(100))