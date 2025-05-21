import streamlit as st
import pandas as pd
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# =====================================================================================================================================


def remove_duplicates(df):
    return df.drop_duplicates()

def fill_null_values(df, method='mean'):
    for column in df.select_dtypes(include='number'):
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
    df.fillna('Unknown', inplace=True)
    return df

def encode_data(df):
    le = LabelEncoder()
    for column in df.select_dtypes(include='object'):
        try:
            df[column] = le.fit_transform(df[column])
        except:
            pass
    return df

def scale_data(df):
    scaler = StandardScaler()
    num_df = df.select_dtypes(include='number')
    df[num_df.columns] = scaler.fit_transform(num_df)
    return df

# =============================================================================================================================================

st.set_page_config(page_title="DataCleaner Pro", layout="wide")

st.title("Data Cleaner Web App ")

uploaded_file = st.file_uploader(" Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader(" Original Data Preview")
    st.dataframe(df.head())

    st.sidebar.title("🛠 Cleaning Options")
    
    if st.sidebar.checkbox("Remove Duplicates"):
        df = remove_duplicates(df)
    
    if st.sidebar.checkbox("Fill Null Values"):
        method = st.sidebar.selectbox("Method", ["mean", "median"])
        df = fill_null_values(df, method)

    if st.sidebar.checkbox("Encode Categorical Columns"):
        df = encode_data(df)

    if st.sidebar.checkbox("Scale/Normalize Numeric Columns"):
        df = scale_data(df)

    st.subheader(" Cleaned Data Preview")
    st.dataframe(df.head())

    st.write(" Shape:", df.shape)

    # Download link
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(" Download Cleaned CSV", data=csv, file_name="cleaned_data.csv", mime='text/csv')
