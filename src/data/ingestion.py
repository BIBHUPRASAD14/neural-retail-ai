import pandas as pd

# Load data from both CSV files, clean column names, and merge into a single DataFrame
def load_data(file_path_1: str, file_path_2: str) -> pd.DataFrame:
    try:
        df1 = pd.read_csv(file_path_1, encoding='ISO-8859-1')
        df2 = pd.read_csv(file_path_2, encoding='ISO-8859-1')

        # Clean column names
        df1.columns = df1.columns.str.strip()
        df2.columns = df2.columns.str.strip()

        # Standardize df2 column names
        df2 = df2.rename(columns={
            "Customer ID": "CustomerID",
            "Invoice": "InvoiceNo",
            "Price": "UnitPrice"
        })

        print("✅ Columns standardized")

        # MERGE HAPPENS HERE
        df = pd.concat([df1, df2], ignore_index=True)

        # ADD THIS LINE RIGHT AFTER MERGE
        df = df[[
            "InvoiceNo", "StockCode", "Description", "Quantity",
            "InvoiceDate", "UnitPrice", "CustomerID", "Country"
        ]]

        print("✅ Datasets merged and cleaned")
        print("📊 Combined shape:", df.shape)

        return df

    except Exception as e:
        print(f"❌ Error: {e}")
        return None