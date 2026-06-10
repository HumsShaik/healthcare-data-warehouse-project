import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data

st.set_page_config(
    page_title="Clinical Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Clinical Analysis")

df = load_data()

condition_df = (
    df.groupby("condition_name")
    .agg(
        total_visits=("visit_key", "count"),
        avg_los=("length_of_stay", "mean")
    )
    .reset_index()
)

col1, col2 = st.columns(2)

fig1 = px.bar(
    condition_df.sort_values("total_visits"),
    x="total_visits",
    y="condition_name",
    orientation="h",
    title="Top Conditions by Visits"
)

col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    condition_df.sort_values("avg_los"),
    x="avg_los",
    y="condition_name",
    orientation="h",
    title="Average Length of Stay by Condition"
)

col2.plotly_chart(fig2, use_container_width=True)