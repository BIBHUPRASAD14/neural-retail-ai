from src.config.config import DATA_PATH_1, DATA_PATH_2, PROCESSED_DATA_PATH
from src.data.ingestion import load_data
from src.data.preprocessing import clean_data
from src.data.validation import validate_data
from src.features.build_features import create_rfm
from src.models.train_segmentation import segment_customers
from src.models.train_churn import train_churn_model
from src.models.save_model import save_model

# Step 1: Load data
df = load_data(DATA_PATH_1, DATA_PATH_2)

# Step 2: Clean data
df_clean = clean_data(df)

# Step 3: Save cleaned data
df_clean.to_csv(PROCESSED_DATA_PATH, index=False)

# Step 4: Validate data
validate_data(df_clean)

# Step 5: Create RFM
rfm = create_rfm(df_clean)

# Step 6: Segmentation
rfm_segmented, kmeans_model = segment_customers(rfm)

# Step 7: Train churn model
churn_model, rfm_with_churn = train_churn_model(rfm_segmented)

# Step 8: Save models
save_model(kmeans_model, "kmeans.pkl")
save_model(churn_model, "churn_model.pkl")

# (AFTER CHURN MODEL)
#print(rfm_with_churn["Churn"].value_counts())

# (AFTER SEGMENTATION)
#print(rfm_segmented.groupby("Cluster").mean())

# Optional: preview data
#print(rfm_segmented.head())

# (AFTER CHURN MODEL)
#print(rfm_with_churn.head())
