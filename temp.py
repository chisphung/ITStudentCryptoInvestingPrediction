import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
try:
    df = pd.read_excel('crypto_survey.xlsx')
except FileNotFoundError:
    st.error("File 'crypto_survey.xlsx' not found. Please check the file path.")
    st.stop()

df_copy = df.copy()  # Copy the dataframe to avoid modifying the original

# Convert categorical columns to binary
binary_cols = ['Safety', 'Blockchain', 'Will_invest', 'Will_learn']
df_copy[binary_cols] = df_copy[binary_cols].map({'Có': 1, 'Không': 0})

df_copy['Year'] = df_copy['Year'].map({'Năm 1': 1, 'Năm 2': 2, 'Năm 3': 3, 'Năm 4': 4})
df_copy['Gender'] = df_copy['Gender'].map({'Nam': 1, 'Nữ': 0})
df_copy['Invested'] = df_copy['Invested'].map(lambda x: 0 if x == 'Không' else 1)

# Features and target selection
X = df_copy.drop(columns=['Will_invest'])  
y = df_copy['Will_invest']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensure 'Invested' column is of integer type
X_train['Invested'] = X_train['Invested'].astype(int)
X_test['Invested'] = X_test['Invested'].astype(int)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Streamlit UI
st.title("Dự đoán khả năng đầu tư vào tiền điện tử")
st.write(f"Dự đoán khả năng đầu tư vào tiền điện tử của sinh viên dựa trên dữ liệu khảo sát (Độ chính xác mô hình: **{accuracy:.2f}**)")

# User inputs
Year = st.selectbox("Năm học", options=[1, 2, 3, 4])
Gender = st.selectbox("Giới tính", options=["Nam", "Nữ"])
Invested = st.selectbox("Đã đầu tư vào tiền điện tử chưa", options=["Có", "Không"])
Safety = st.selectbox("Cảm thấy an toàn khi đầu tư vào tiền điện tử", options=["Có", "Không"])
Blockchain = st.selectbox("Biết về Blockchain", options=["Có", "Không"])
Will_learn = st.selectbox("Có muốn học về tiền điện tử không", options=["Có", "Không"])

# Convert inputs to numerical format
Gender = 1 if Gender == "Nam" else 0
Invested = 1 if Invested == "Có" else 0
Safety = 1 if Safety == "Có" else 0
Blockchain = 1 if Blockchain == "Có" else 0
Will_learn = 1 if Will_learn == "Có" else 0

# Create input dataframe
a_student = pd.DataFrame([{
    "Year": Year, 
    "Gender": Gender, 
    "Invested": Invested,
    "Safety": Safety,
    "Blockchain": Blockchain,
    "Will_learn": Will_learn
}]).astype(int)

# Make prediction
prediction = model.predict(a_student)[0]

# Display result
st.subheader("Kết quả dự đoán:")
if prediction == 1:
    st.success("Sinh viên này có khả năng sẽ đầu tư vào tiền điện tử.")
else:
    st.warning("Sinh viên này không có khả năng đầu tư vào tiền điện tử.")
