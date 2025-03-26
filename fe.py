import streamlit as st

st.title("Dự đoán khả năng đầu tư vào tiền điện tử")
# st.write(f"Dự đoán khả năng đầu tư vào tiền điện tử của sinh viên dựa trên dữ liệu khảo sát (Độ chính xác mô hình: **{accuracy:.2f}**)")

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
