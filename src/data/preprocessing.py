import pandas as pd

# Clean data by removing invalid entries, handling missing values, and creating new features
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("🔹 Initial shape:", df.shape)

    # Fix column names (safety)
    df.columns = df.columns.str.strip()

    # Remove missing CustomerID
    df = df.dropna(subset=["CustomerID"])

    # Remove invalid values
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors='coerce')

    # Remove null dates if any
    df = df.dropna(subset=["InvoiceDate"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Create TotalPrice
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    print("✅ Cleaned shape:", df.shape)

    return df