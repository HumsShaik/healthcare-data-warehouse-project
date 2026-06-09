-- Query 1 - Executive KPIs -- demonstrates Aggregation and Business KPIs
SELECT
    COUNT(*) AS total_visits,
    SUM(cost) AS total_cost,
    AVG(cost) AS avg_cost,
    AVG(length_of_stay) AS avg_length_of_stay,
    AVG(satisfaction) AS avg_satisfaction
FROM fact_patient_visit;

-- Query 2 - condition analysis  -- Demonstrates JOIN, GROUP BY, ORDER BY
SELECT
    dc.condition_name,
    COUNT(*) AS total_patients,
    SUM(fpv.cost) AS total_cost,
    AVG(fpv.length_of_stay) AS avg_length_of_stay
FROM fact_patient_visit fpv
JOIN dim_condition dc
    ON fpv.condition_key = dc.condition_key
GROUP BY dc.condition_name
ORDER BY total_cost DESC;

-- Query 3 - Procedure analysis  -- 

SELECT
    dp.procedure_name,
    COUNT(*) AS procedure_count,
    AVG(fpv.cost) AS avg_cost
FROM fact_patient_visit fpv
JOIN dim_procedure dp
    ON fpv.procedure_key = dp.procedure_key
GROUP BY dp.procedure_name
ORDER BY procedure_count DESC;

-- Query 4 - Readmission Impact

SELECT
    dr.readmission_status,
    COUNT(*) AS total_visits,
    AVG(cost) AS avg_cost,
    AVG(length_of_stay) AS avg_los
FROM fact_patient_visit fpv
JOIN dim_readmission dr
    ON fpv.readmission_key = dr.readmission_key
GROUP BY dr.readmission_status;

-- Query 5 - Outcome analysis

SELECT
    doo.outcome_status,
    COUNT(*) AS total_patients,
    AVG(cost) AS avg_cost,
    AVG(satisfaction) AS avg_satisfaction
FROM fact_patient_visit fpv
JOIN dim_outcome doo
    ON fpv.outcome_key = doo.outcome_key
GROUP BY doo.outcome_status;

-- Query 6 - window function (RANK)

SELECT
    patient_key,
    cost,
    RANK() OVER (
        ORDER BY cost DESC
    ) AS cost_rank
FROM fact_patient_visit;

-- Query 7 - ROW_NUMBER -- demonstrates ROW_NUMBER()

SELECT
    patient_key,
    cost,
    ROW_NUMBER() OVER (
        ORDER BY cost DESC
    ) AS row_num
FROM fact_patient_visit;

-- Query 8 - Cost Category (CASE WHEN) -- demonstrates CASE WHEN and Business Rules

SELECT
    patient_key,
    cost,
    CASE
        WHEN cost < 5000 THEN 'Low Cost'
        WHEN cost < 10000 THEN 'Medium Cost'
        ELSE 'High Cost'
    END AS cost_category
FROM fact_patient_visit;

-- Query 9 - CTE -- Demonstrates CTE and Reusable Query Logic

WITH condition_costs AS (
    SELECT
        dc.condition_name,
        SUM(fpv.cost) AS total_cost
    FROM fact_patient_visit fpv
    JOIN dim_condition dc
        ON fpv.condition_key = dc.condition_key
    GROUP BY dc.condition_name
)

SELECT *
FROM condition_costs
ORDER BY total_cost DESC;

-- Query 10: Top 5 Most Expensive Conditions

SELECT
    dc.condition_name,
    SUM(fpv.cost) AS total_cost
FROM fact_patient_visit fpv
JOIN dim_condition dc
    ON fpv.condition_key = dc.condition_key
GROUP BY dc.condition_name
ORDER BY total_cost DESC
LIMIT 5;

