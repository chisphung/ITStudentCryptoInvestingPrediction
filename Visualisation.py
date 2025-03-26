import streamlit as st
import pandas as pd 
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_excel('crypto_survey.xlsx')
# print(df.head())

df_copy = df.copy()  # Make a copy to keep the original data safe
binary_cols = ['Safety', 'Blockchain', 'Will_invest', 'Will_learn']

for col in binary_cols:
    df_copy[col] = df_copy[col].map({'Có': 1, 'Không': 0})

df_copy['Year'] = df_copy['Year'].map({'Năm 1': 1, 'Năm 2': 2, 'Năm 3': 3, 'Năm 4': 4})
df_copy['Gender'] = df_copy['Gender'].map({'Nam': 1, 'Nữ': 0})

df_copy.loc[df_copy['Invested'] == 'Không', 'Invested'] = 0
df_copy.loc[df_copy['Invested'] != 'Không', 'Invested'] = 1



X = df_copy.drop(columns=['Will_invest'])  # Features
y = df_copy['Will_invest'] # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train['Invested'] = X_train['Invested'].astype(int)
X_test['Invested'] = X_test['Invested'].astype(int)
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))

st.title("Dự đoán khả năng đầu tư vào tiền mã hóa")
st.write("Dự đoán khả năng đầu tư vào tiền mã hóa của sinh viên dựa trên dữ liệu khảo sát 150 sinh viên")

Year = st.selectbox("Năm học", options=[1, 2, 3, 4])
Gender = st.selectbox("Giới tính", options=["Nam", "Nữ"])
Invested = st.selectbox("Đã đầu tư vào tiền mã hóa", options=["Có", "Không"])
Safety = st.selectbox("Cảm thấy tiền mã hóa an toàn", options=["Có", "Không"])
Blockchain = st.selectbox("Biết về  công nghệ Blockchain", options=["Có", "Không"])
Will_learn = st.selectbox("Có muốn học về tiền điện tử ", options=["Có", "Không"])

Gender = 1 if Gender == "Nam" else 0
Invested = 1 if Invested == "Có" else 0
Safety = 1 if Safety == "Có" else 0
Blockchain = 1 if Blockchain == "Có" else 0
Will_learn = 1 if Will_learn == "Có" else 0

# a_student = {"Year": 2, "Gender": 0, "Invested": 0,	"Safety": 1,	"Blockchain": 1,	"Will_learn": 1}

# print(model.predict(a_student))
if st.button("Dự đoán"):
    a_student = {"Year": Year, "Gender": Gender, "Invested": Invested,	"Safety": Safety,	"Blockchain": Blockchain,	"Will_learn": Will_learn}
    a_student = pd.DataFrame([a_student]).astype(int)
    prediction = model.predict(a_student)
    if prediction == 1:
        st.success("Sinh viên này có khả năng đầu tư vào tiền mã hóa")
    else:
        st.info("Sinh viên này không có khả năng đầu tư vào tiền mã hóa")


