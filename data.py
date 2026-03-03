import pandas as pd

def load_deadlines(path="deadlines.csv"):
    df = pd.read_csv(path)
    
    # Melt from wide to long format
    df_long = df.melt(id_vars="uid", var_name="date", value_name="count")
    
    # Drop zero entries
    df_clean = df_long[df_long["count"] > 0].reset_index(drop=True)
    
    # Parse dates
    df_clean["date"] = pd.to_datetime(df_clean["date"])
    
    return df_clean

if __name__ == "__main__":
    df = load_deadlines()
    print(df.head())
    print(f"\nShape: {df.shape}")
