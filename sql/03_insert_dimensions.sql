INSERT INTO dim_patient (
    patient_id,
    age,
    gender
)
SELECT DISTINCT
    patient_id,
    age,
    gender
FROM stg_healthcare;


INSERT INTO dim_condition (
    condition_name
)
SELECT DISTINCT
    condition
FROM stg_healthcare;


INSERT INTO dim_procedure (
    procedure_name
)
SELECT DISTINCT
    procedure_name
FROM stg_healthcare;


INSERT INTO dim_readmission (
    readmission_status
)
SELECT DISTINCT
    readmission
FROM stg_healthcare;


INSERT INTO dim_outcome (
    outcome_status
)
SELECT DISTINCT
    outcome
FROM stg_healthcare;

SELECT COUNT(*) FROM dim_patient;
SELECT COUNT(*) FROM dim_condition;
SELECT COUNT(*) FROM dim_procedure;
SELECT COUNT(*) FROM dim_readmission;
SELECT COUNT(*) FROM dim_outcome;