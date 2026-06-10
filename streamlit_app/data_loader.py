import pandas as pd
from pathlib import Path

def load_data():
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "processed" / "healthcare_tableau_dataset.csv"

    df = pd.read_csv(file_path)

    return df