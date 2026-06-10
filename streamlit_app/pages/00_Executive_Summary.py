import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import engine

st.set_page_config(
    page_title="Executive Summary",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Executive Summary")

kpi_query = """
SELECT
    COUNT(*) AS total_visits,
    SUM(cost) AS total_cost,
    AVG(cost) AS avg_cost,
    AVG(length_of_stay) AS avg_length_of_stay,
    AVG(satisfaction) AS avg_satisfaction
FROM fact_patient_visit;
"""

kpi_df = pd.read_sql(kpi_query, engine)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Visits", f"{kpi_df['total_visits'][0]:,.0f}")
col2.metric("Total Cost", f"${kpi_df['total_cost'][0]:,.0f}")
col3.metric("Avg Cost", f"${kpi_df['avg_cost'][0]:,.2f}")
col4.metric("Avg LOS", f"{kpi_df['avg_length_of_stay'][0]:.2f}")
col5.metric("Avg Satisfaction", f"{kpi_df['avg_satisfaction'][0]:.2f}")

st.divider()

condition_query = """
SELECT
    dc.condition_name,
    SUM(fpv.cost) AS total_cost
FROM fact_patient_visit fpv
JOIN dim_condition dc
    ON fpv.condition_key = dc.condition_key
GROUP BY dc.condition_name
ORDER BY total_cost DESC;
"""

condition_df = pd.read_sql(condition_query, engine)

fig1 = px.bar(
    condition_df,
    x="total_cost",
    y="condition_name",
    orientation="h",
    title="Total Cost by Condition",
    labels={
        "total_cost": "Total Cost",
        "condition_name": "Condition"
    }
)

fig1.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig1, use_container_width=True)

outcome_query = """
SELECT
    doo.outcome_status,
    COUNT(*) AS total_visits
FROM fact_patient_visit fpv
JOIN dim_outcome doo
    ON fpv.outcome_key = doo.outcome_key
GROUP BY doo.outcome_status;
"""

outcome_df = pd.read_sql(outcome_query, engine)

fig2 = px.bar(
    outcome_df,
    x="outcome_status",
    y="total_visits",
    title="Visits by Outcome",
    labels={
        "outcome_status": "Outcome",
        "total_visits": "Total Visits"
    }
)

st.plotly_chart(fig2, use_container_width=True)