<div align='center'>
    <h1><b>FlightBuddy</b></h1>
    <img src='deployment/companyLogo.png'/>
    <br><br>
    <p>This project is focused on creating a Natural Language Processing (NLP) model that can determine if reviews are positive or negative (performing sentiment analysis) and provide recommendations based on the results.</p>
    <br>

![Python](https://badgen.net/badge/Python/3.9.18/blue?)
![Streamlit](https://badgen.net/badge/Streamlit/1.10.0/orange?)
![Pandas](https://badgen.net/badge/Pandas/1.4.3/blue?)
![Seaborn](https://badgen.net/badge/Seaborn/0.11.2/green?)
![Matplotlib](https://badgen.net/badge/Matplotlib/3.5.2/blue?)
![Scikit-learn](https://badgen.net/badge/scikit-learn/1.4.2/yellow?)
![Plotly](https://badgen.net/badge/Plotly/5.22.0/cyan?)
![TensorFlow](https://badgen.net/badge/TensorFlow/2.15.0/orange?)
![WordCloud](https://badgen.net/badge/WordCloud/1.8.1/purple?)
![NLTK](https://badgen.net/badge/NLTK/3.7/red?)
![Docker](https://badgen.net/badge/Docker/20.10/cyan?)

</div>

---

## 🧑‍💻 **Team Members**

- **Livia Amanda Annafiah**
  - Role: Data Scientist and Data Engineer  
  - [Github](https://github.com/liviamanda) | [LinkedIn](https://www.linkedin.com/in/liviaamanda/)

- **Alfarabi**
  - Role: Data Analyst and Data Scientist  
  - [Github](https://github.com/Alfarabi58) | [LinkedIn](https://www.linkedin.com/in/alfa-rabi-49b9b8285/)
  
- **Badriah Nursakinah**
  - Role: Data Analyst  
  - Github | LinkedIn

<br />

## 💾 **Dataset**

The dataset is obtained from a credible source and comprises relevant details regarding airline reviews. For further information or to access the dataset, please refer to the provided source [here](https://www.kaggle.com/datasets/juhibhojani/airline-reviews/data).

<br />

## ⚠️ **Problem Statement**

Choosing the right airline can greatly affect a traveler's overall experience, including comfort, service quality, and in-flight amenities. With many online reviews available, airline passengers often rely on these reviews to make informed decisions about which airline to choose. However, the large number of reviews can make it difficult and time-consuming to read through and understand the general opinion about an airline.

FlightBuddy aims to solve this problem by using advanced Natural Language Processing (NLP) techniques to analyze airline reviews quickly and accurately. By processing and understanding a large number of reviews, FlightBuddy can determine whether the opinions in the reviews are positive or negative.

<br />

## 📌 **Objective**

The main goal of FlightBuddy is to improve the decision-making process for travelers by providing personalized airline recommendations based on the analysis of review sentiments. Specifically, FlightBuddy aims to:
- Analyze the sentiment of airline reviews to classify them as positive or negative, with accuracy serving as the metric.
- Recommend five airlines with similar positive characteristics for users who have seen favorable reviews.
- Suggest top-rated alternative airlines for users who have encountered negative experiences, ensuring they have better options for future travel.

<br />

---

## 🗒️ **Installation**

### Local Installation in Visual Studio Code:

1. **Clone the Repository**
   - Clone the repository to your local machine using Git:
     ```
     git clone https://github.com/username/repo
     ```

2. **Navigate to the Repository Directory**
   - Change directory to the cloned repository:
     ```
     cd repo
     ```

3. **Open Visual Studio Code**
   - Open the project directory in Visual Studio Code:
     ```
     code .
     ```

4. **Set Up a Python Virtual Environment (optional)**
   - It's a good practice to use a virtual environment for Python projects. Here’s how to set up one in Visual Studio Code:
     - Open the terminal in Visual Studio Code (Ctrl+` or View -> Terminal).
     - Install the virtual environment if you haven't installed it:
       ```
       pip install virtualenv
       ```
     - Create a virtual environment:
       ```
       virtualenv venv
       ```
     - Activate the virtual environment:
       - On Windows:
         ```
         .\venv\Scripts\activate
         ```
       - On MacOS/Linux:
         ```
         source venv/bin/activate
         ```

5. **Install Dependencies**
   - Install the required Python packages using pip:
     ```
     pip install -r requirements.txt
     ```

6. **Run the Application**
   - Run the Python script or application:
     ```
     python main.py
     ```

### Installation via Docker:

If you prefer to use Docker, follow these steps:

1. **Build the Docker Image**
   - Build an image from the Dockerfile present in your project directory:
     ```
     docker build -t app .
     ```

2. **Run the Docker Container**
   - Run your application inside a Docker container:
     ```
     docker run -it app
     ```

### Run Remotely via Docker:

To run the Docker image from a remote repository:

1. **Pull and Run the Docker Image**
   - Pull the image from Docker Hub and run it:
     ```
     docker pull username/dockerimage:version
     docker run -it username/dockerimage:version
     ```

<br />

---

## 🔎 **SHOWCASE**

Additional images, gifs, or videos of your project.

<br />

---

## 💻 **Tools and Libraries**

![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-%238DD6F9.svg?style=for-the-badge&logo=seaborn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23D00000.svg?style=for-the-badge&logo=matplotlib&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-%232376C6.svg?style=for-the-badge&logo=nltk&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![WordCloud](https://img.shields.io/badge/WordCloud-%23FF8800.svg?style=for-the-badge&logo=wordcloud&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-%23157AF6.svg?style=for-the-badge&logo=textblob&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white)

<br />

---

## 📌 **LINKS**

[<img alt="Github" src="https://img.shields.io/badge/[username]-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/[username])
[<img alt="Twitter" src="https://img.shields.io/badge/[username]-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white" />](https://twitter.com/[username])
[<img alt="Instagram" src="https://img.shields.io/badge/[username]-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white" />](https://instagram.com/[username])
[<img alt="Youtube" src="https://img.shields.io/badge/[username]-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" />](https://www.youtube.com/channel/[username])

[<img alt="Reddit" src="https://img.shields.io/badge/[username]-FF4500?style=for-the-badge&logo=reddit&logoColor=white" />](https://reddit.com/user/[username])
[<img alt="TikTok" src="https://img.shields.io/badge/[username]-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white" />](https://www.tiktok.com/@[username])
[<img alt="Gitlab" src="https://img.shields.io/badge/[username]-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white" />](https://gitlab.com/[username])
[<img alt="Dribbble" src="https://img.shields.io/badge/[username]-EA4C89?style=for-the-badge&logo=dribbble&logoColor=white" />](https://dribbble.com/[username])

[<img alt="Stack Overflow" src="https://img.shields.io/badge/[username]-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white" />](https://stackoverflow.com/users/[usercode]/[username])
[<img alt="Discord" src="https://img.shields.io/badge/[username%23code]-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white" />]()
[<img alt="Steam" src="https://img.shields.io/badge/[username]-%23000000.svg?style=for-the-badge&logo=steam&logoColor=white" />](https://steamcommunity.com/id/[username])
[<img alt="Spotify" src="https://img.shields.io/badge/[username]-1ED760?style=for-the-badge&logo=spotify&logoColor=white" />](https://open.spotify.com/user/[username])

