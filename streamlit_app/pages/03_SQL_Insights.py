import streamlit as st
import pandas as pd
from data_loader import load_data

st.set_page_config(
    page_title="SQL Insights",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 SQL Insights")

df = load_data()

condition_costs = (
    df.groupby("condition_name")
    .agg(
        total_visits=("visit_key", "count"),
        total_cost=("cost", "sum"),
        avg_cost=("cost", "mean"),
        avg_los=("length_of_stay", "mean")
    )
    .reset_index()
    .sort_values("total_cost", ascending=False)
)

st.subheader("Condition Cost Analysis")

st.dataframe(
    condition_costs,
    use_container_width=True
)

top_cost = (
    df.sort_values("cost", ascending=False)
    .head(20)
)

st.subheader("Top 20 Most Expensive Visits")

st.dataframe(
    top_cost,
    use_container_width=True
)