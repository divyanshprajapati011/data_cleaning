# 🧼 DataCleaner Pro – A Smart Data Cleaning Web App

## 🔷 Project Overview

**DataCleaner Pro** is a powerful and user-friendly **Python + Streamlit-based web application** that automates and simplifies the data cleaning process. Users can upload a CSV file and interactively apply multiple cleaning operations via a graphical interface.

This app is useful for:

* Data scientists
* Data analysts
* Machine learning engineers
* Students working with real-world datasets

---

## 🎯 Features

| Category               | Feature                   | Description                                                                       |
| ---------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| 📤 Upload              | CSV File Input            | Upload any `.csv` file for cleaning                                               |
| 🔁 Duplicate Handling  | Remove Duplicates         | Remove exact duplicate rows                                                       |
| ⚠️ Missing Data        | Fill Null Values          | Fill numeric missing values with `mean` or `median`; categorical with `'Unknown'` |
| 🔠 Encoding            | Label Encoding            | Encode categorical columns using `LabelEncoder`                                   |
| 📊 Scaling             | Standardization           | Scale numeric features using `StandardScaler`                                     |
| 🧪 Outliers            | Outlier Removal           | Remove rows with outliers using the IQR method                                    |
| 🧹 Text Cleaning       | Clean Text Columns        | Remove punctuation, lowercase text, strip whitespace (column selection supported) |
| 🔍 Feature Pruning     | Remove Irrelevant Columns | Select columns manually to remove                                                 |
| 🧬 Feature Engineering | Row Sum Feature           | Adds a new feature by summing numeric columns per row                             |
| 🧾 Rename Columns      | Manual Rename             | Select a column to rename and provide new name input                              |
| 🧭 Indexing            | Set/Reset Index           | Set or reset index based on selected column                                       |

---

## 🛠 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend/Data Processing**: `pandas`, `sklearn`, `imblearn`, `string`
* **Machine Learning Models**:

  * `IsolationForest` for anomaly detection
  * `SMOTE` from `imblearn` for class balancing
* **Deployment Ready**: Compatible with Streamlit Cloud or local servers

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/DataCleanerPro.git
cd DataCleanerPro

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```




## 📄 How It Works

1. Launch the app using `streamlit run app.py`
2. Upload your `.csv` file
3. Use sidebar checkboxes to apply cleaning operations
4. Configure settings for each operation (e.g., select columns to clean)
5. View live preview of the cleaned data
6. Download the cleaned dataset

---

## 📁 File Structure

```
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## 🙋‍♂️ Developed By

> **Deepak Prajapati**
> Python Developer | Data Science Enthusiast

📧 Email: \[[deepakprajapat7067@gmail.com]]
🌐 GitHub: [https://github.com/yourusername](https://github.com/divyanshprajapati011)
📍 Location: India

---

## 📝 License

This project is licensed under the MIT License. Feel free to use and modify it for your learning or professional work.
