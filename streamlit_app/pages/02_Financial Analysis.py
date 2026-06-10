import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import engine

st.set_page_config(page_title="Financial Analysis", page_icon="💰", layout="wide")

st.title("💰 Financial Analysis")

procedure_query = """
SELECT
    dp.procedure_name,
    SUM(fpv.cost) AS total_cost,
    AVG(fpv.cost) AS avg_cost
FROM fact_patient_visit fpv
JOIN dim_procedure dp
    ON fpv.procedure_key = dp.procedure_key
GROUP BY dp.procedure_name
ORDER BY total_cost DESC;
"""

procedure_df = pd.read_sql(procedure_query, engine)

readmission_query = """
SELECT
    dr.readmission_status,
    AVG(fpv.cost) AS avg_cost,
    COUNT(*) AS total_visits
FROM fact_patient_visit fpv
JOIN dim_readmission dr
    ON fpv.readmission_key = dr.readmission_key
GROUP BY dr.readmission_status;
"""

readmission_df = pd.read_sql(readmission_query, engine)

col1, col2 = st.columns(2)

fig1 = px.bar(
    procedure_df,
    x="total_cost",
    y="procedure_name",
    orientation="h",
    title="Total Cost by Procedure"
)
fig1.update_layout(yaxis={"categoryorder": "total ascending"})
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    readmission_df,
    x="readmission_status",
    y="avg_cost",
    title="Readmission vs Average Cost"
)
col2.plotly_chart(fig2, use_container_width=True)