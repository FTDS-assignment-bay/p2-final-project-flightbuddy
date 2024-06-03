# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load English stopwords
stopwords_eng = set(stopwords.words('english'))

# Additional Stopwords
additional_stopwords = ['the', 'to', 'and', 'I', 'was', 'a', 'in', 'of', 'for', 'on', 'flight', 'with', 'that', 'my', 'is', 'not', 'were', 'they',
                    'The', 'at', 'we', 'had', 'from', 'but', 'have', 'it', 'this', 'no', 'as', 'me', 'you', 'our', 'be', 'are', 'an', 'very', 'so',
                    'service', 'their', 'We', 'time', 'airline', 'would', 'or', 'us', 'by', 'only', 'get', 'all', 'which']

# Extend stopwords list
stopwords_eng.update(additional_stopwords)

# Load the pre-trained model
model_path = os.path.join('unzipped_model', 'model_logreg')
model = load_model(model_path)

# Define WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the data
df = pd.read_csv('avg_ratings_per_airline.csv')

# Function for text preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'https?://(?:www\.[^\s\n\r]+|[^\s\n\r]+)', '', text)  # Remove URLs
    text = re.sub(r'#', '', text)  # Remove hashtags
    text = re.sub(r'[\n\r]', '', text)  # Remove newlines
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub("[^A-Za-z\s']", " ", text)  # Remove non-letters
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [word for word in tokens if word not in stopwords_eng]  # Remove stopwords
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatize tokens
    return ' '.join(tokens)  # Join tokens back to text

# Normalize the ratings
scaler = StandardScaler()

rating_columns = ['avg_seat_comfort', 'avg_cabin_staff_service', 'avg_food_beverages', 'avg_ground_service',
                  'avg_inflight_entertainment', 'avg_wifi_connectivity', 'avg_value_for_money']

normalized_data = scaler.fit_transform(df[rating_columns])

# Compute cosine similarity
similarity_matrix = cosine_similarity(normalized_data)

# Convert the similarity matrix to a DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=df['airline_name'], columns=df['airline_name'])

# Function to get recommendations based on cosine similarity
def get_similar_airlines(airline, n_recommendations=5):

    # Get the similarity scores for the specified airline with all others
    similar_scores = similarity_df[airline].sort_values(ascending=False)

    # Remove the airline itself from the recommendation
    similar_scores = similar_scores.drop(airline)

    # Get the top N similar airlines
    top_airlines = similar_scores.head(n_recommendations)
    return top_airlines

def run():
    st.title('Airplane Review Analysis')
    st.subheader('Sentiment Analysis and Recommendation System')
    st.markdown('---')

    # Dropdown to select airline names
    selected_airline = st.selectbox("Select an Airline", df['airline_name'])

    # Input form for feedback
    with st.form(key='review_sentiment_detect'):
        st.write(f"## Feedback for {selected_airline}")
        review_text = st.text_input("Enter Your Review:")
        submitted = st.form_submit_button('Analyze Feedback')

        if submitted:
            # Preprocess the input text
            processed_text = preprocess_text(review_text)

            # Perform sentiment analysis
            input_data = {'text': processed_text}
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df['text'])
            predicted_label = np.argmax(prediction)

            # Display sentiment analysis result
            if predicted_label == 0:
                st.error("Negative Feedback - Not Recommended")
                st.subheader("Top 5 Airlines Recommendations:")
                st.write("Since this feedback indicates a less positive experience, here are top 5 airlines recommended by reviewers:")
                similar_airlines = get_similar_airlines(selected_airline)
                st.write(similar_airlines)
                
            elif predicted_label == 1:
                st.success("Positive Feedback - Recommended")
                st.subheader("Similar Airlines Recommendations:")
                st.write("Since this feedback indicates a positive experience, here are 5 similar airlines:")
                similar_airlines = get_similar_airlines(selected_airline)
                st.write(similar_airlines)

            st.subheader("Extracted Feedback Text:")
            st.write(review_text)

if __name__ == '__main__':
    run()