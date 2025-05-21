import streamlit as st
import pandas as pd
import string
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import IsolationForest
from imblearn.over_sampling import SMOTE

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

def convert_data_types(df, conversions):
    for col, dtype in conversions.items():
        try:
            df[col] = df[col].astype(dtype)
        except:
            pass
    return df

def detect_outliers(df):
    for col in df.select_dtypes(include='number'):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]
    return df

def fix_inconsistencies(df):
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip().str.lower()
    return df

def remove_irrelevant_features(df, threshold=0.01):
    variances = df.var(numeric_only=True)
    low_var_cols = variances[variances < threshold].index.tolist()
    return df.drop(columns=low_var_cols)

def feature_engineering(df):
    df['row_sum'] = df.select_dtypes(include='number').sum(axis=1)
    return df

def clean_text_columns(df):
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.replace('[{}]'.format(string.punctuation), '', regex=True)
        df[col] = df[col].str.lower().str.strip()
    return df

def parse_dates(df):
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass
    return df

def balance_classes(df, target_col):
    sm = SMOTE()
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    X_res, y_res = sm.fit_resample(X, y)
    return pd.concat([pd.DataFrame(X_res), pd.DataFrame(y_res, columns=[target_col])], axis=1)

def detect_anomalies(df):
    iso = IsolationForest()
    numeric_cols = df.select_dtypes(include='number')
    preds = iso.fit_predict(numeric_cols)
    df['anomaly'] = preds
    return df[df['anomaly'] == 1].drop(columns='anomaly')

def rename_columns(df, rename_dict):
    return df.rename(columns=rename_dict)

def reset_index(df):
    return df.reset_index(drop=True)

def set_index(df, column):
    return df.set_index(column)

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

if st.sidebar.checkbox("Fix Inconsistencies"):
    df = fix_inconsistencies(df)

if st.sidebar.checkbox("Detect & Remove Outliers"):
    df = detect_outliers(df)

if st.sidebar.checkbox("Remove Irrelevant Features"):
    df = remove_irrelevant_features(df)

if st.sidebar.checkbox("Feature Engineering (row_sum)"):
    df = feature_engineering(df)

if st.sidebar.checkbox("Text Cleaning"):
    df = clean_text_columns(df)

if st.sidebar.checkbox("Date Parsing"):
    df = parse_dates(df)

if st.sidebar.checkbox("Detect Anomalies"):
    df = detect_anomalies(df)

if st.sidebar.checkbox("Rename Columns"):
    rename_dict = st.text_area("Enter column rename dict (e.g. {'old':'new'})")
    if rename_dict:
        df = rename_columns(df, eval(rename_dict))

if st.sidebar.checkbox("Reset Index"):
    df = reset_index(df)

if st.sidebar.checkbox("Set Index"):
    column = st.selectbox("Select Column to Set as Index", df.columns)
    df = set_index(df, column)

    st.subheader(" Cleaned Data Preview")
    st.dataframe(df.head())

    st.write(" Shape:", df.shape)

# Download link
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(" Download Cleaned CSV", data=csv, file_name="cleaned_data.csv", mime='text/csv')
