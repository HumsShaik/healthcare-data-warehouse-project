COPY stg_healthcare (
    patient_id,
    age,
    gender,
    condition,
    procedure_name,
    cost,
    length_of_stay,
    readmission,
    outcome,
    satisfaction
)
FROM 'C:/Projects/DataAnalysis/healthcare-data-warehouse-project/data/raw/hospital data analysis.csv'
DELIMITER ','
CSV HEADER;