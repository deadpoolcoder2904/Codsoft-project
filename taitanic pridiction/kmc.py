import streamlit as st
import numpy as np
import pandas as pd 

st.title('Titanic Survival Prediction')

st.sidebar.header('User Input Features')

def user_input_features():
 Pclass = st.sidebar.selectbox('Pclass', (1, 2, 3))
 Sex = st.sidebar.selectbox('Sex', ('male', 'female'))
 Age = st.sidebar.text_input('Age', 0, 80, 29)
# if Age==text_input:
#       Age="Age"
# else:
#      Age="invalid"
# SibSp = st.sidebar.slider('SibSp', 0, 8, 0)
# Parch = st.sidebar.slider('Parch', 0, 6, 0)
# Fare = st.sidebar.slider('Fare', 0, 513, 32)
# Embarked = st.sidebar.selectbox('Embarked', ('C', 'Q', 'S'))

# data = {
#         'Pclass': Pclass,
#         'Sex': Sex,
#         'Age': Age,
#         'SibSp': SibSp,
#         'Parch': Parch,
#         'Fare': Fare,
#         'Embarked': Embarked
#     }
# features = pd.DataFrame(data, index=[0])
# # return features

# input_df = user_input_features()

# # Encode and preprocess the user input features
# input_df['Sex'] = input_df['Sex'].map({'male': 0, 'female': 1})
# input_df = pd.get_dummies(input_df, columns=['Embarked'])
# input_df = input_df.reindex(columns=features, fill_value=0)

# Display user input features
# st.subheader('User Input features')
# st.write(input_df)

# Predictsurvival
# prediction = model.predict(input_df)
# prediction_proba = model.predict_proba(input_df)

# st.subheader('Prediction')
# st.write('Survived' if prediction[0] == 1 else 'Did not survive')

# st.subheader('Prediction Probability')
# st.write(prediction_proba)