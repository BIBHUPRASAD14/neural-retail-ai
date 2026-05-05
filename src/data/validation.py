import pandas as pd

# Validate data by checking for missing values, invalid entries, and ensuring required columns are present
def validate_data(df: pd.DataFrame):
    print("🔹 Validating data...")

    # Check missing values
    if df.isnull().sum().sum() > 0:
        print("⚠️ Warning: Missing values found")

    # Check negative values
    if (df["Quantity"] <= 0).any():
        print("⚠️ Warning: Invalid Quantity found")

    if (df["UnitPrice"] <= 0).any():
        print("⚠️ Warning: Invalid UnitPrice found")

    # Check required columns
    required_cols = [
        "InvoiceNo", "StockCode", "Quantity",
        "InvoiceDate", "UnitPrice", "CustomerID"
    ]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"❌ Missing column: {col}")

    print("✅ Data validation completed")

    return True