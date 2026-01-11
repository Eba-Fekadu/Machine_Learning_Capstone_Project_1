import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from pathlib import Path

# 1. Load Data 
def load_data(filename="solar_data.csv"):
    """Load dataset ."""
    base_path = Path(__file__).resolve().parents[1]   
    data_path = base_path / "data" / filename

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    print(f"Loading dataset from: {data_path}")
    return pd.read_csv(data_path)


# 2. Extract Time Features

def extract_time_features(df):
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    df["Hour"] = df["Timestamp"].dt.hour
    df["Day"] = df["Timestamp"].dt.day
    df["Month"] = df["Timestamp"].dt.month
    df["DayOfYear"] = df["Timestamp"].dt.dayofyear

    return df


# 3. Encode Cleaning Column

def encode_cleaning(df):
    df["Cleaning"] = df.get("Cleaning", "No").map({"Yes": 1, "No": 0}).fillna(0)
    return df



# 4. Encode ALL Categorical Columns 
def encode_categorical(df):
    """Encode all non-numeric columns using Label Encoding."""
    label_encoders = {}

    for col in df.columns:
        if df[col].dtype == "object":   # detect string columns
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le

    return df, label_encoders


# 5. Derived Features

def create_derived_features(df):
    df["WSgust_ratio"] = (
        df["WSgust"] / (df["WS"] + 0.001) 
        if "WS" in df.columns and "WSgust" in df.columns 
        else 0
    )

    df["HeatIndex"] = (
        df["Tamb"] * df["RH"] 
        if "Tamb" in df.columns and "RH" in df.columns 
        else 0
    )

    return df



# 6. Drop Irrelevant Columns

def drop_irrelevant(df):
    drop_cols = ["Comments", "Outlier", "WDstdev", "Timestamp"]
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore")
    return df


# 7. Clean Numeric Columns

def clean_numeric(df):
    """Fix NaN, Inf, and zero-variance columns before scaling."""

    # Replace Inf → NaN
    df = df.replace([np.inf, -np.inf], np.nan)

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

    # Fill NaN with mean
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # Drop zero-variance columns
    zero_var_cols = [col for col in numeric_cols if df[col].std() == 0]

    if zero_var_cols:
        print("Dropping zero-variance columns:", zero_var_cols)
        df = df.drop(columns=zero_var_cols)

    return df



# 8. Scale Numeric Features 

def scale_features(df):
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, scaler



# 9. Full Pipeline

def process_data(filename="solar_data.csv"):
    df = load_data(filename)

    df = extract_time_features(df)
    df = encode_cleaning(df)

    #  encode Country and other categorical columns
    df, label_encoders = encode_categorical(df)

    df = create_derived_features(df)
    df = drop_irrelevant(df)
    df = clean_numeric(df)
    df, scaler = scale_features(df)

    return df, scaler, label_encoders



# 10. Run Script

if __name__ == "__main__":
    base_path = Path(__file__).resolve().parents[1]
    output_path = base_path / "data" / "solar_processed.csv"

    df, scaler, label_encoders = process_data()
    df.to_csv(output_path, index=False)

    print(f"\nProcessing complete. Saved to:\n{output_path}\n")
