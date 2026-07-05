import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Convert TotalCharges to numeric
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    # Handle missing values
    df["totalcharges"].fillna(df["totalcharges"].median(), inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert target variable
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

    return df

if __name__ == "__main__":
    from config import DATA_RAW_PATH, DATA_PROCESSED_PATH

    df = load_data(DATA_RAW_PATH)
    df_cleaned = clean_data(df)
    df_cleaned.to_csv(DATA_PROCESSED_PATH, index=False)