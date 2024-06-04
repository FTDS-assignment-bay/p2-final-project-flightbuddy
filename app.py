import eda
import predict
import streamlit as st

# Add side bar for navigation
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Review Predictor'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''This tool is designed to explore and predict airline reviews. It employs advanced data analysis and machine learning models to offer insights and predictions that can assist users in understanding and analyzing airline reviews.''')

# Features
st.sidebar.write('''### Key Features:
- **Exploratory Data Analysis**: Analyze the data to uncover patterns and insights related to airline reviews.
- **Review Predictor**: Use predictive models to forecast the sentiment of airline reviews.''')

# Target Audience
st.sidebar.write('''### Who can benefit?
- **Travelers**: Understand sentiments about airlines from various reviews.
- **Airline Companies**: Analyze and improve customer satisfaction based on reviews.
- **Data Scientists**: Develop and evaluate machine learning models for review sentiment prediction.''')

# Tools
st.sidebar.write('''### Tools Utilized:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `TensorFlow/Keras`: For implementing machine learning models.''')

# Define the Home Page
def show_home():
    st.title('Welcome to Airline Review Analysis Tool')
    st.write('''This tool provides functionalities for Exploratory Data Analysis and Prediction regarding airline reviews. Use the navigation pane on the left to select the module you wish to utilize.''')
    st.image('logo 2.png', caption='Source: Canva')
    st.markdown('---')
    st.write('#### 📈 Dataset')
    st.markdown('''The dataset is sourced reliably and contains pertinent information on airline reviews. For additional details or to download the dataset, visit the provided source.''')
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''Airlines face challenges in understanding customer satisfaction through reviews. This tool helps in analyzing and predicting sentiments from reviews, enabling airlines to improve their services.''')
    st.write('#### 💡 Objective')
    st.markdown('''This project focuses on creating a classification model to predict review sentiments, selecting the best performer among various models. The key evaluation metric for assessing model performance is accuracy.''')



# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Review Predictor':
    predict.run()