import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data

st.set_page_config(
    page_title="Financial Analysis",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Financial Analysis")

df = load_data()

procedure_df = (
    df.groupby("procedure_name")
    .agg(
        total_cost=("cost", "sum"),
        avg_cost=("cost", "mean")
    )
    .reset_index()
)

readmission_df = (
    df.groupby("readmission_status")
    .agg(
        avg_cost=("cost", "mean"),
        total_visits=("visit_key", "count")
    )
    .reset_index()
)

col1, col2 = st.columns(2)

fig1 = px.bar(
    procedure_df.sort_values("total_cost"),
    x="total_cost",
    y="procedure_name",
    orientation="h",
    title="Total Cost by Procedure"
)

col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    readmission_df,
    x="readmission_status",
    y="avg_cost",
    title="Readmission vs Average Cost"
)

col2.plotly_chart(fig2, use_container_width=True)