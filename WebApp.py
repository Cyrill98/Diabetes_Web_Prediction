import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

import streamlit as st

st.write("""
# Diabetes Detection
Detect if someone has diabetes using machine learning
""")

image = Image.open('Images\diabetes.jpeg')
st.image(image, caption='ML', use_column_width = True)

# Get the data
df = pd.read_csv('diabetes.csv')

# Set subheader
st.subheader('Data Information')

# Show the data as a table
st.dataframe(df)

#Shoe statistics on the data
st.write(df.describe())

# Show data as chart
chart = st.bar_chart(df)

# Split data into x and y variables
X = df.iloc[:, 0:8].values
Y = df.iloc[:, -1].values

# Split dataset test and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

# Get user input
def get_user_input():
    pregnancies = st.sidebar.slider('pregnancies', 0, 10, 5)
    glucose = st.sidebar.slider('glucose', 0, 199, 117)
    blood_pressure = st.sidebar.slider('blood_pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('skin_thickness', 0, 99, 23)
    insulin = st.sidebar.slider('insulin', 0.0, 846.0, 30.0)
    BMI = st.sidebar.slider('BMI', 0.0, 67.1, 32.0)
    DPF = st.sidebar.slider('DPF', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('age', 21, 81, 29)


    # Store dictionary into variable
    user_data = {'pregnancies': pregnancies,
                 'glucose': glucose,
                 'blood_pressure': blood_pressure,
                 'skin_thickness': skin_thickness,
                 'insulin': insulin,
                 'BMI':BMI,
                 'DPF': DPF,
                 'age': age}
    # Transform data into dataframe
    features = pd.DataFrame(user_data, index = [0])
    return features

# Store user input into variables
user_input = get_user_input()

# Set subheader and display user input
st.subheader('User Input: ')
st.write(user_input)

# Create and train the model
RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train, Y_train)

# Show model metrics
st.subheader('Model Test Accuracy Score: ')
st.write( str(accuracy_score(Y_test, RandomForestClassifier.predict(X_test)) * 100) + '%')

# Store model prediction in a variable
prediction = RandomForestClassifier.predict(user_input)

# Set subheader and display classification
st.subheader('Classification: ')
st.write(prediction)