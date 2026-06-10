import streamlit as st

st.set_page_config(
    page_title="Project Overview",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Project Overview")

st.markdown("""
## Healthcare Data Warehouse & Analytics Project

This project demonstrates an end-to-end healthcare analytics workflow using:

- **PostgreSQL**
- **Advanced SQL**
- **Data Warehouse Design**
- **Star Schema Modeling**
- **Python**
- **Streamlit**
- **Tableau**
- **GitHub**

---

## Project Objective

The goal of this project is to transform raw healthcare patient data into a structured analytics-ready data warehouse and create dashboards for business, clinical, and financial insights.

---

## Data Warehouse Architecture

Raw CSV Data  
⬇️  
SQL Staging Table  
⬇️  
Dimension Tables  
⬇️  
Fact Table  
⬇️  
Advanced SQL Analysis  
⬇️  
Python Validation  
⬇️  
Tableau & Streamlit Dashboards  

---

## Star Schema Design

### Dimension Tables

- `dim_patient`
- `dim_condition`
- `dim_procedure`
- `dim_readmission`
- `dim_outcome`

### Fact Table

- `fact_patient_visit`

### Measures

- Cost
- Length of Stay
- Satisfaction
- Visit Count

---

## Key Business Questions Answered

- What are the most common patient conditions?
- Which procedures drive the highest costs?
- How does readmission affect average cost?
- Which conditions are associated with longer hospital stays?
- How do patient outcomes relate to satisfaction?

---

## Skills Demonstrated

### SQL

- Staging tables
- Dimension tables
- Fact tables
- Primary keys
- Foreign keys
- Joins
- CTEs
- Window functions
- Aggregations
- CASE statements

### Data Warehousing

- Star schema design
- ETL workflow
- Surrogate keys
- Fact and dimension modeling
- Analytics-ready schema design

### Visualization

- Tableau executive dashboard
- Tableau clinical dashboard
- Tableau financial dashboard
- Streamlit interactive dashboard

---

## Final Deliverables

- PostgreSQL healthcare data warehouse
- SQL ETL scripts
- Advanced SQL analysis scripts
- Python validation notebook
- Tableau dashboards
- Streamlit dashboard
- GitHub documentation
""")

st.success("This project is designed as a professional SQL + Healthcare Data Warehouse portfolio project.")