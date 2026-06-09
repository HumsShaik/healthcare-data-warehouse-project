INSERT INTO fact_patient_visit (
    patient_key,
    condition_key,
    procedure_key,
    readmission_key,
    outcome_key,
    cost,
    length_of_stay,
    satisfaction,
    visit_count
)
SELECT
    p.patient_key,
    c.condition_key,
    pr.procedure_key,
    r.readmission_key,
    o.outcome_key,
    s.cost,
    s.length_of_stay,
    s.satisfaction,
    1
FROM stg_healthcare s

JOIN dim_patient p
    ON s.patient_id = p.patient_id

JOIN dim_condition c
    ON s.condition = c.condition_name

JOIN dim_procedure pr
    ON s.procedure_name = pr.procedure_name

JOIN dim_readmission r
    ON s.readmission = r.readmission_status

JOIN dim_outcome o
    ON s.outcome = o.outcome_status;

	SELECT COUNT(*)
FROM fact_patient_visit;

SELECT *
FROM fact_patient_visit
LIMIT 10

SELECT SUM(cost)
FROM fact_patient_visit;

SELECT AVG(length_of_stay)
FROM fact_patient_visit;