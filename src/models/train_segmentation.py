from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Train a customer segmentation model using KMeans on RFM features
def segment_customers(rfm):
    print("🔹 Starting customer segmentation...")

    # Select features
    X = rfm[["Recency", "Frequency", "Monetary"]]

    # Scale data (VERY IMPORTANT)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply KMeans
    kmeans = KMeans(n_clusters=4, random_state=42)
    rfm["Cluster"] = kmeans.fit_predict(X_scaled)

    print("✅ Segmentation completed")

    return rfm, kmeans