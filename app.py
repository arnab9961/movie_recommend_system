import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Movie Recommendation App",
    page_icon="🎬",
)

st.sidebar.success("Select a page above.")




page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



def recommend_content(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = movies)dct[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dct = pickle.load(open('movies_dct.pkl','rb'))
movies = pd.DataFrame(movies_dct)



st.title('Movie Recommendation System')

movies_name = st.selectbox(
    'which movies do you like?',
    movies['title'].values)



col1, col2 = st.columns([1,1])

with col1:
    if st.button('Recommendation'):
        recommendations = recommend_content(movies_name)
        for i in recommendations:
            st.write(i)

