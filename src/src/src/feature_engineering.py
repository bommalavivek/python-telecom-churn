import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-1 year", "1-2 years", "2-4 years", "4+ years"]
    )

    df["is_high_value_customer"] = df["monthlycharges"] > df["monthlycharges"].median()

    return df