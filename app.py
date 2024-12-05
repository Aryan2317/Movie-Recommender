import streamlit as st
import pickle


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new.df.iloc[i[0]].title)
    return recommended_movies

# Streamlit page configuration
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommender System")
st.write("""
Welcome to the Movie Recommender System! 🎥
Enter a movie title to get recommendations for similar movies.
""")

with st.form(key='movie_form'):
    st.subheader("Enter a Movie Title")
    movie_title = st.text_input("Movie Title", placeholder="e.g., Inception")
    submit_button = st.form_submit_button("Get Recommendations")

if submit_button and movie_title:
    recommendations = recommend(movie_title)  # Fixed function name
    st.write(f"### Recommendations for '{movie_title}':")
    st.write("Here are some movies you might like:")
    for movie in recommendations:
        st.markdown(f"- **{movie}**")

st.markdown("""
<style>
    .stApp {
        background-color: #f0f4f8;
    }
    .stTitle {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .css-1x7p2vw {
        font-family: 'Arial', sans-serif;
    }
    .stTextInput>div>input {
        border: 2px solid #3498db;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stTextInput>div>input:focus {
        border-color: #2980b9;
        box-shadow: 0 0 5px rgba(41, 128, 185, 0.5);
    }
</style>
""", unsafe_allow_html=True)
