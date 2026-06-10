import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data

st.set_page_config(
    page_title="Executive Summary",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Executive Summary")

df = load_data()

# KPI Calculations
total_visits = df["visit_key"].count()
total_cost = df["cost"].sum()
avg_cost = df["cost"].mean()
avg_los = df["length_of_stay"].mean()
avg_satisfaction = df["satisfaction"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Visits", f"{total_visits:,.0f}")
col2.metric("Total Cost", f"${total_cost:,.0f}")
col3.metric("Avg Cost", f"${avg_cost:,.2f}")
col4.metric("Avg LOS", f"{avg_los:.2f}")
col5.metric("Avg Satisfaction", f"{avg_satisfaction:.2f}")

st.divider()

# Cost by Condition
condition_df = (
    df.groupby("condition_name")["cost"]
    .sum()
    .reset_index()
    .sort_values("cost", ascending=False)
)

fig1 = px.bar(
    condition_df,
    x="cost",
    y="condition_name",
    orientation="h",
    title="Total Cost by Condition"
)

fig1.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig1, use_container_width=True)

# Visits by Outcome
outcome_df = (
    df.groupby("outcome_status")["visit_key"]
    .count()
    .reset_index(name="total_visits")
)

fig2 = px.bar(
    outcome_df,
    x="outcome_status",
    y="total_visits",
    title="Visits by Outcome"
)

st.plotly_chart(fig2, use_container_width=True)