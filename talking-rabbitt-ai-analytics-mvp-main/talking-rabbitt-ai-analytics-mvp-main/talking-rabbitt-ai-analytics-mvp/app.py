import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

# ✅ ADD THIS EMAIL FUNCTION HERE (RIGHT AFTER IMPORTS)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(to_email, subject, message):

    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

    email = Mail(
        from_email="h97732716@gmail.com",  # must verify in SendGrid
        to_emails=to_email,
        subject=subject,
        plain_text_content=message
    )

    response = sg.send(email)
    return response.status_code



# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Talking Rabbitt Analytics",
    layout="wide"
)

st.title("🐰 Talking Rabbitt - Conversational Analytics")

# ================= FILE UPLOAD =================
uploaded_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Make a working copy (important for cleaning without breaking original)
    df_clean = df.copy()

# report = df_clean.to_csv(index=False)

# st.download_button(
#     "⬇ Download Report",
#     report,
#     file_name="sales_report.csv",
#     mime="text/csv"
# )

    # ================= DATASET =================
    st.subheader("Dataset Preview")
    st.dataframe(df_clean)

    # ================= KPI DASHBOARD =================
    st.subheader("📊 KPI Dashboard")

    col1, col2, col3 = st.columns(3)

    # Customers
    with col1:
        if "CustomerID" in df_clean.columns:
            st.metric(
                "Customers",
                len(df_clean["CustomerID"].unique())
            )
        else:
            st.metric("Customers", "N/A")

    # Products
    with col2:
        if "Product" in df_clean.columns:
            st.metric(
                "Products",
                len(df_clean["Product"].unique())
            )
        else:
            st.metric("Products", "N/A")

    # Revenue
    with col3:
        if "Revenue" in df_clean.columns:
            total_sales = df_clean["Revenue"].sum()
            st.metric(
                "Revenue",
                f"₹{total_sales:,.2f}"
            )
        else:
            total_sales = 0
            st.metric("Revenue", "N/A")

    # ================= AI INSIGHTS =================
    st.subheader("⭐ AI Generated Insights")

    growth = 0
    top_product = "N/A"

    if "Revenue" in df_clean.columns:
        total_sales = df_clean["Revenue"].sum()
        mean_sales = df_clean["Revenue"].mean()

        # Safe growth calculation
        if total_sales != 0:
            growth = (mean_sales / total_sales) * 100
        else:
            growth = 0

        st.success(f"📈 Sales activity score: {growth:.1f}%")

    if "Product" in df_clean.columns:
        top_product = df_clean["Product"].value_counts().idxmax()
        st.success(f"🔥 {top_product} has highest demand")

    st.warning("⚠ Customer retention dropped by 8% (simulated insight)")

    # ================= DAILY REPORT =================
    st.subheader("📄 Automated Daily Report")

    if st.button("Generate Daily Report"):

        st.write("### Business Summary")

        st.write(f"💰 Total Sales: ₹{total_sales:,.2f}")
        st.write(f"🔥 Top Product: {top_product}")
        st.write(f"📈 Growth Score: {growth:.2f}%")

    # ================= CUSTOMER SCORING =================
    st.subheader("⭐ Lead / Customer Scoring")

    if "CustomerID" in df_clean.columns and "Revenue" in df_clean.columns:

        score_df = df_clean.groupby("CustomerID")["Revenue"].sum().reset_index()

        max_revenue = score_df["Revenue"].max()

        score_df["Score"] = (
            score_df["Revenue"] / max_revenue * 100
        ).fillna(0).astype(int)

        score_df = score_df.sort_values(by="Score", ascending=False)

        st.dataframe(score_df[["CustomerID", "Score"]])

    # ================= CRM TRACKING =================
    st.subheader("📌 CRM Lead Status Tracking")

    if "CustomerID" in df_clean.columns and "Revenue" in df_clean.columns:

        crm = df_clean.groupby("CustomerID")["Revenue"].sum().reset_index()

        def assign_status(x):
            if x < 1000:
                return "New"
            elif x < 3000:
                return "Contacted"
            elif x < 5000:
                return "Interested"
            else:
                return "Converted"

        crm["Status"] = crm["Revenue"].apply(assign_status)

        st.dataframe(crm[["CustomerID", "Status"]])

    # ================= DATA CLEANING =================
    st.subheader("🧹 Data Cleaning Automation")

    if st.button("Clean Data"):

        original_rows = len(df_clean)

        df_clean = df_clean.drop_duplicates()

        removed = original_rows - len(df_clean)

        for col in df_clean.columns:
            if df_clean[col].dtype == "object":
                df_clean[col] = df_clean[col].fillna("Unknown")
            else:
                df_clean[col] = df_clean[col].fillna(df_clean[col].mean())

        st.success(f"✅ {removed} duplicates removed")
        st.dataframe(df_clean.head())

    # ================= CUSTOMER SEGMENTATION =================
    st.subheader("👥 Customer Segmentation")

    if "CustomerID" in df_clean.columns and "Revenue" in df_clean.columns:

        segment_df = df_clean.groupby("CustomerID")["Revenue"].sum().reset_index()

        def segment(x):
            if x > 5000:
                return "Premium"
            elif x > 2000:
                return "Regular"
            return "New"

        segment_df["Segment"] = segment_df["Revenue"].apply(segment)

        st.dataframe(segment_df[["CustomerID", "Segment"]])

    # ================= SALES FORECAST =================
    st.subheader("📈 Sales Forecast")

    if "Revenue" in df_clean.columns:
        predicted = df_clean["Revenue"].mean() * 1.10

        st.metric(
            "Predicted Sales",
            f"₹{predicted:.2f}"
        )

    # ================= NOTIFICATIONS =================
    # ================= NOTIFICATIONS =================
# ================= NOTIFICATIONS =================
st.subheader("📩 Notifications")

notification = st.selectbox(
    "Notification Type",
    ["Email", "WhatsApp"]
)

email = st.text_input("Customer Email")
subject = st.text_input("Subject", "Talking Rabbitt Update")
message = st.text_area("Message", "Hello! Here is your update.")

if st.button("Send Email"):

    if not email:
        st.error("Enter email address")

    else:
        try:
            send_email(email, subject, message)
            st.success(f"📧 Email sent to {email}")

        except Exception as e:
            st.error(f"❌ Failed: {e}")

# ✅ DOWNLOAD MUST BE OUTSIDE BUTTON
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

csv = convert_df(df_clean)

st.download_button(
    "⬇ Download Report",
    csv,
    "sales_report.csv",
    "text/csv"
)
