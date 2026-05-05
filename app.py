import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(page_title="Neural Retail AI", layout="wide")

# -------------------------------
# LOAD DATA (FIRST)
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/clean_data.csv")

df = load_data()

# -------------------------------
# LOAD MODELS (FIRST)
# -------------------------------
kmeans = joblib.load("models/kmeans.pkl")
churn_model = joblib.load("models/churn_model.pkl")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Go to",
    ["Overview", "Segmentation", "Churn Prediction"]
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🛒 Neural Retail AI Dashboard")
st.markdown("AI-powered customer segmentation & churn prediction")

# -------------------------------
# PAGE CONTROL
# -------------------------------

if page == "Overview":

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", len(df))
    col2.metric("Unique Customers", df["CustomerID"].nunique())
    col3.metric("Total Revenue", f"{df['Quantity'].mul(df['UnitPrice']).sum():,.0f}")

    st.subheader("📈 Sales Distribution")
    fig = px.histogram(df, x="Quantity")
    st.plotly_chart(fig, use_container_width=True)


elif page == "Segmentation":

    st.subheader("👥 Customer Segmentation Insight")

    rfm = df.groupby("CustomerID").agg({
        "InvoiceNo": "count",
        "Quantity": "sum"
    }).reset_index()

    rfm.columns = ["CustomerID", "Frequency", "Monetary"]

    fig2 = px.scatter(
        rfm,
        x="Frequency",
        y="Monetary",
        title="Customer Behavior Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)


elif page == "Churn Prediction":

    st.subheader("🔮 Predict Customer Churn")

    col1, col2, col3 = st.columns(3)

    recency = col1.number_input("Recency", min_value=0, value=50)
    frequency = col2.number_input("Frequency", min_value=0, value=10)
    monetary = col3.number_input("Monetary", min_value=0, value=1000)

    if st.button("Predict Churn"):
        pred = churn_model.predict([[recency, frequency, monetary]])

        if pred[0] == 1:
            st.error("⚠️ High Risk: Customer likely to churn")
        else:
            st.success("✅ Customer likely to stay")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("Built with ❤️ using Machine Learning & Streamlit")