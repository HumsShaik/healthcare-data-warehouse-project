DROP TABLE IF EXISTS fact_patient_visit;
DROP TABLE IF EXISTS dim_patient;
DROP TABLE IF EXISTS dim_condition;
DROP TABLE IF EXISTS dim_procedure;
DROP TABLE IF EXISTS dim_readmission;
DROP TABLE IF EXISTS dim_outcome;
DROP TABLE IF EXISTS stg_healthcare;

CREATE TABLE stg_healthcare (
    patient_id INT,
    age INT,
    gender VARCHAR(20),
    condition VARCHAR(100),
    procedure_name VARCHAR(100),
    cost NUMERIC(12,2),
    length_of_stay INT,
    readmission VARCHAR(10),
    outcome VARCHAR(50),
    satisfaction INT
);

CREATE TABLE dim_patient (
    patient_key SERIAL PRIMARY KEY,
    patient_id INT UNIQUE,
    age INT,
    gender VARCHAR(20)
);

CREATE TABLE dim_condition (
    condition_key SERIAL PRIMARY KEY,
    condition_name VARCHAR(100) UNIQUE
);

CREATE TABLE dim_procedure (
    procedure_key SERIAL PRIMARY KEY,
    procedure_name VARCHAR(100) UNIQUE
);

CREATE TABLE dim_readmission (
    readmission_key SERIAL PRIMARY KEY,
    readmission_status VARCHAR(10) UNIQUE
);

CREATE TABLE dim_outcome (
    outcome_key SERIAL PRIMARY KEY,
    outcome_status VARCHAR(50) UNIQUE
);

CREATE TABLE fact_patient_visit (
    visit_key SERIAL PRIMARY KEY,
    patient_key INT REFERENCES dim_patient(patient_key),
    condition_key INT REFERENCES dim_condition(condition_key),
    procedure_key INT REFERENCES dim_procedure(procedure_key),
    readmission_key INT REFERENCES dim_readmission(readmission_key),
    outcome_key INT REFERENCES dim_outcome(outcome_key),
    cost NUMERIC(12,2),
    length_of_stay INT,
    satisfaction INT,
    visit_count INT DEFAULT 1
);