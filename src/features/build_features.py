import pandas as pd

def create_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create RFM features from transaction data
    """

    print("🔹 Creating RFM features...")

    # Snapshot date (latest date in dataset)
    snapshot_date = df["InvoiceDate"].max()

    # Group by CustomerID
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": "count",
        "TotalPrice": "sum"
    })

    # Rename columns
    rfm.columns = ["Recency", "Frequency", "Monetary"]

    print("✅ RFM created")
    print("📊 RFM shape:", rfm.shape)

    return rfm.reset_index()