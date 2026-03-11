import pandas as pd

def load_dataset():

    df = pd.read_csv("dataset/dataset.csv")

    numeric_columns = [
        "Watch time(Minutes)",
        "Stream time(minutes)",
        "Peak viewers",
        "Average viewers",
        "Followers",
        "Followers gained",
        "Views gained"
    ]

    for col in numeric_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )

        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df