# IT Student Awareness about Cryptocurrency, a project for SS004.P27
A survey conducted on 150 IT students asking about their awareness and their point of view toward cryptocurrency
## Task management: 
We distributed tasks among members, held meetings, and discussed the topic. Each member actively took on tasks, and our operational plan was written in a sheet:  
![image](https://github.com/user-attachments/assets/572b6df3-d1d9-4473-a886-c7b4e71ecae2)
## Pipeline
![Survey data (2)](https://github.com/user-attachments/assets/5e509b99-d631-47b0-9fbf-867cbb88bb00)
## Web development
### Data preprocessing
Binary columns were converted to values of 0 and 1, representing `Yes` and `No`, respectively. The `Year` values were also modified to numerical values (`1, 2, 3, 4`) instead of text in the raw data.  
This process facilitates model training. 
```py
binary_cols = ['Safety', 'Blockchain', 'Will_invest', 'Will_learn']

for col in binary_cols:
    df_copy[col] = df_copy[col].map({'Có': 1, 'Không': 0})

df_copy['Year'] = df_copy['Year'].map({'Năm 1': 1, 'Năm 2': 2, 'Năm 3': 3, 'Năm 4': 4})
df_copy['Gender'] = df_copy['Gender'].map({'Nam': 1, 'Nữ': 0})

df_copy.loc[df_copy['Invested'] == 'Không', 'Invested'] = 0
df_copy.loc[df_copy['Invested'] != 'Không', 'Invested'] = 1
```
### Training
Use ```X``` to store ```Feature``` and ```y``` to store ```Target``` to be predicted. The preprocessed data was splited into test and train set using ```train_test_split``` from ```sklearn``` library.
```test_size``` and ```random_state``` were predefined to ```0.2``` and ```42```, respectively, due to the small dataset.
```py
X = df_copy.drop(columns=['Will_invest'])  # Features
y = df_copy['Will_invest'] # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train['Invested'] = X_train['Invested'].astype(int)
X_test['Invested'] = X_test['Invested'].astype(int)
```
The model was choosen was RandomForest. I tested on both RandomForest and XGBoost and resulted in 0.7 of accuracy based on ```accuracy_score``` provided by ```sklearn```
Load the model and start the training process: 
```py
model = RandomForestClassifier()
model.fit(X_train, y_train)
```
### Web constructing
I used Streamlit to deploy the web application. Users input their basic information, which is then passed to the trained model.
The result is displayed after the user clicks the "Predict" button.
## Disclaimer
This is a small project implemented by a group of students, and some survey results might be inaccurate. Please use the predictions with caution.
If you find this project helpful, please give it a star and contribute by filling out the survey if you are an IT student.

[Survey Link](https://forms.gle/7ZqBRXjbqUMQFKrs5)

Our website is being deployed at the following link:

[Try it](https://itcoin.streamlit.app/)
