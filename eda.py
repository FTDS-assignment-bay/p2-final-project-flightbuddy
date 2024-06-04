# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define custom color palette
custom_palette = px.colors.qualitative.Set3

# Function to generate word cloud
def generate_wordcloud(text, title, ax):
    if text.strip():  # Check if text is not empty
        wordcloud = WordCloud(width=400, height=200, background_color='white').generate(text)
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_title(title, size=15)
        ax.axis('off')
    else:
        ax.text(0.5, 0.5, 'No words available', horizontalalignment='center', verticalalignment='center', size=15, color='red')
        ax.set_title(title, size=15)
        ax.axis('off')

# Create the main program
def run():
    # Load the dataset
    data = pd.read_csv('airline_review_cleaned.csv')
    
    # Add title to the app
    st.title('Exploratory Data Analysis on Airline Reviews')
    
    # Checkbox to display raw data
    if st.checkbox('Show raw data'):
        st.markdown('#### Raw Data')
        st.write(data)
    
    # Dropdown for different analysis options
    option = st.selectbox('Select Analysis', ('Overview', 'Distribution Plots', 'Categorical Analysis', 'Correlation Heatmap', 'Word Cloud'))
    
    # Overview analysis
    if option == 'Overview':
        st.subheader('Dataset Overview')
        st.write('This dataset contains reviews from airline passengers along with their ratings on various aspects of the flight.')
        st.markdown('###### Summary Statistics')
        numerical_columns = data[['overall_rating', 'seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money']]
        st.write(numerical_columns.describe())
    
    # Distribution plots analysis
    elif option == 'Distribution Plots':
        st.subheader('Distribution of Numerical Variables')
        numerical_columns = st.multiselect('Select columns to visualize', ['overall_rating', 'seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money'], 
                                           ['overall_rating', 'seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money'])
        
        for idx, col in enumerate(numerical_columns):
            fig = px.histogram(data, x=col, title=f'Distribution of {col.title().replace("_", " ")}', nbins=30, color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
    
    # Categorical analysis
    elif option == 'Categorical Analysis':
        st.subheader('Categorical Data Analysis')
        categorical_columns = st.multiselect('Select columns to visualize', ['verified', 'type_of_traveller', 'seat_type', 'recommended'], 
                                             ['type_of_traveller', 'verified','seat_type', 'recommended'])
        
        for idx, col in enumerate(categorical_columns):
            fig = px.histogram(data, x=col, title=f'{col.title().replace("_", " ")} Distribution', color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)

    # Word cloud analysis
    elif option == 'Word Cloud':
        st.subheader('Word Cloud Analysis')
        
        wordcloud_options = st.multiselect('Select Word Cloud', ['All Reviews', 'Recommended (Yes)', 'Recommended (No)'], ['All Reviews'])
        
        if wordcloud_options:
            fig, axes = plt.subplots(len(wordcloud_options), 1, figsize=(10, 5 * len(wordcloud_options)))
            if len(wordcloud_options) == 1:
                axes = [axes]  # Make sure axes is iterable
            
            for idx, wordcloud_option in enumerate(wordcloud_options):
                if wordcloud_option == 'All Reviews':
                    all_text = ' '.join(data['review'].dropna())
                    generate_wordcloud(all_text, 'Word Cloud - All Reviews', axes[idx])
                
                elif wordcloud_option == 'Recommended (Yes)':
                    recommended_yes_text = ' '.join(data[data['recommended'] == 'yes']['review'].dropna())
                    generate_wordcloud(recommended_yes_text, 'Word Cloud - Recommended (Yes)', axes[idx])
                
                elif wordcloud_option == 'Recommended (No)':
                    recommended_no_text = ' '.join(data[data['recommended'] == 'no']['review'].dropna())
                    generate_wordcloud(recommended_no_text, 'Word Cloud - Recommended (No)', axes[idx])
            
            plt.subplots_adjust(hspace=0.3)
            st.pyplot(fig)

    # Correlation heatmap analysis
    elif option == 'Correlation Heatmap':
        st.subheader('Correlation Heatmap')
        numerical_columns = data[['seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money']]
        corr = numerical_columns.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax)
        st.pyplot(fig)
        st.markdown('The correlation heatmap shows the relationships between various aspects of the airline reviews.')

# Run the app
if __name__ == '__main__':
    run()
