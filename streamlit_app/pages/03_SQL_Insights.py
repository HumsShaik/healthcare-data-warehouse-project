import streamlit as st
import pandas as pd
from db_connection import engine

st.set_page_config(page_title="SQL Insights", page_icon="🧾", layout="wide")

st.title("🧾 SQL Insights")

st.markdown("This page displays advanced SQL outputs from the healthcare data warehouse.")

query = """
WITH condition_costs AS (
    SELECT
        dc.condition_name,
        COUNT(*) AS total_visits,
        SUM(fpv.cost) AS total_cost,
        AVG(fpv.cost) AS avg_cost,
        AVG(fpv.length_of_stay) AS avg_los
    FROM fact_patient_visit fpv
    JOIN dim_condition dc
        ON fpv.condition_key = dc.condition_key
    GROUP BY dc.condition_name
)
SELECT *
FROM condition_costs
ORDER BY total_cost DESC;
"""

df = pd.read_sql(query, engine)

st.subheader("Condition Cost Analysis using CTE")
st.dataframe(df, use_container_width=True)

rank_query = """
SELECT
    visit_key,
    patient_key,
    cost,
    RANK() OVER (
        ORDER BY cost DESC
    ) AS cost_rank
FROM fact_patient_visit
LIMIT 20;
"""

rank_df = pd.read_sql(rank_query, engine)

st.subheader("Top Cost Visits using Window Function")
st.dataframe(rank_df, use_container_width=True)