import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import engine

st.set_page_config(page_title="Clinical Analysis", page_icon="📊", layout="wide")

st.title("📊 Clinical Analysis")

condition_query = """
SELECT
    dc.condition_name,
    COUNT(*) AS total_visits,
    AVG(fpv.length_of_stay) AS avg_los
FROM fact_patient_visit fpv
JOIN dim_condition dc
    ON fpv.condition_key = dc.condition_key
GROUP BY dc.condition_name
ORDER BY total_visits DESC;
"""

condition_df = pd.read_sql(condition_query, engine)

col1, col2 = st.columns(2)

fig1 = px.bar(
    condition_df,
    x="total_visits",
    y="condition_name",
    orientation="h",
    title="Top Conditions by Visits"
)
fig1.update_layout(yaxis={"categoryorder": "total ascending"})
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    condition_df.sort_values("avg_los", ascending=False),
    x="avg_los",
    y="condition_name",
    orientation="h",
    title="Average Length of Stay by Condition"
)
fig2.update_layout(yaxis={"categoryorder": "total ascending"})
col2.plotly_chart(fig2, use_container_width=True)