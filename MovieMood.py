import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

st.set_page_config(layout="wide", page_title="MovieMood", page_icon=":film_frames:")

st.markdown(
    """
    <style>
        div[data-testid="stLinkButton"] p
        {
            font-size: 0.8rem !important;
        } 

        div[data-testid="stLinkButton"]
        {
            text-align: center;
        }

        div[data-testid="stButton"]
        {
            text-align: end;
        } 

        /* Breakpoints for More Details sections below movie posters */
        @media only screen and (min-width: 768px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 200px;
            }
        }

        @media only screen and (min-width: 1000px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 200px;
            }
        }

        @media only screen and (min-width: 1100px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 250px;
            }
        }

        @media only screen and (min-width: 1300px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 350px;
            }
        }

        @media only screen and (min-width: 1600px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 400px;
            }
        }

        @media only screen and (min-width: 1800px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 500px;
            }
        }

        @media only screen and (min-width: 2000px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 550px;
            }
        }

        @media only screen and (min-width: 2200px) {
            div[data-testid="column"] div[data-testid="stImage"] {
                height: 650px;
            }
        }

        div[data-testid="stExpanderDetails"] div[data-testid="column"] {
            border: 1px gray solid;
            padding: 30px;
        }

        .block-container {
            padding-top: 30px;
        }

        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="stImage"] {
            height: 0px;
        }

        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="stStyledFullScreenFrame"] div {
            justify-content: right;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def get_data(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("successfully fetched the data")
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
        return response.json()
    except:
        return {'movies_list': [], 'spotify_information': []}


# Set up the title & introduction!

col1,col2 = st.columns([3, 1])
with col1:
    st.write(f' <p style="font-size:2.75rem;font-weight:700;padding-top:10px"> Welcome to MovieMood </p>',unsafe_allow_html=True)
with col2:
    # st.image("images/logo.jpg", width=250)
    st.image("images/logo.jpg")


st.write(f' <p style="font-size:1rem;font-style: italic;"> At MovieMood, we strive to bridge the gap between music and movies, and enrich users\' emotional journeys, to create a uniquely personalized and curated multimedia experience. </p>',unsafe_allow_html=True)

"""
MovieMood uses your Spotify playlist to recommend movies that match your mood. Navigate to the Behind the Scenes page on the left-side menu to learn more about how we generate your recommendations. 
#
"""

"""
To get your recommendations, you will need to upload a CSV file containing your Spotify playlist details.
Instructions to retrieve your CSV file:
1. Navigate to www.exportify.net. 
2. Log in with your Spotify credentials.
3. Select and download the playlist that you would like to use.
"""

# Define the file uploader and filters
uploaded_file = st.file_uploader("Upload your Spotify playlist CSV file below:")

filter_genres = []
filter_ratings = []
filter_imdb_score = 5

    

# if 'drop_movies' not in st.session_state:
#     st.session_state.drop_movies = []

if 'all_movies' not in st.session_state:
    st.session_state.all_movies = []

# if 'persisted_drops' not in st.session_state:
#     st.session_state.persisted_drops = []



st.write(f'<br><br>',unsafe_allow_html=True)


# Get the movie recommendations and display them
if uploaded_file is not None:

    # Pull the spotify CSV file and reformat the music data for the API call
    df = pd.read_csv(uploaded_file)
    arr = df.to_numpy()
    data = {
        "music_list":[["Danceability","Energy","Key","Loudness","Mode","Speechiness","Acousticness","Instrumentalness","Liveness","Valence","Tempo","Time Signature"]]
    }
    for item in arr:
        list_str = list(item)[-12:]
        new_list = []
        for num in list_str:
            new_list.append(str(num))
        data['music_list'].append(new_list)

    # Define remaining API parameters
    url = "https://neilprabhu.mids255.com/predict"
    headers = {"Content-Type": "application/json"}




    # Create title & button header above the recommendation
    col1,col2=st.columns(2)
    with col1:
        st.write(f' <p style="font-size: 1.3rem;font-weight: 600;"> Movie Recommendations </p>',unsafe_allow_html=True)
    with col2:
        # Set up the button to regenerate the recommendations
        if st.button("↻ Regenerate Recommendations", key="regenerate"):

            data['drop_movies'] = st.session_state.all_movies
            data["filter_ratings"] = list(filter_ratings)
            data["filter_genres"] = [x.lower() for x in list(filter_genres)]
            data["imdb_ratings"] = filter_imdb_score

            recs = get_data(url, headers, data)

    with st.expander("See optional filters for movie recommendations"):
        filter_genres = st.multiselect(
            'What are your preferred movie genres? (If none are selected, MovieMood will predict your preferred genre)',
            ['Action',
            'Adventure',
            'Animation',
            'Biography',
            'Comedy',
            'Crime',
            'Documentary',
            'Drama',
            'Family',
            'Fantasy',
            'History',
            'Horror',
            'Music',
            'Musical',
            'Mystery',
            'Romance',
            'Sci-Fi',
            'Short',
            'Thriller',
            'Sport',
            'War'])

        filter_ratings = st.multiselect(
            'What are your preferred movie ratings?',
            ['G', 'PG', 'PG-13', 'R', 'Not Rated'])
    
        
        filter_imdb_score = st.radio(
                "What is your preferred minimum IMDB score?",
                [5, 6, 7, 8, 9],
                horizontal=True
            )
        





    # Add the filter selections to the data for the API call
    data["filter_ratings"] = list(filter_ratings)
    data["filter_genres"] = [x.lower() for x in list(filter_genres)]
    data["imdb_ratings"] = filter_imdb_score

    # Call the API to get the movie recs
    recs = get_data(url, headers, data)









    # Display the movie recommendations & details

    col1,col2,col3,col4,col5=st.columns(5)
    cols=[col1,col2,col3,col4,col5]
    
    for i in range(0,len(recs['movies_list'])):
        with cols[i]:
            title = recs['movies_list'][i]['omdb_title']
            poster = recs['movies_list'][i]['omdb_poster']
            plot = recs['movies_list'][i]['omdb_plot']
            genres = recs['movies_list'][i]['genres']
            director = recs['movies_list'][i]['omdb_director']
            actors = recs['movies_list'][i]['omdb_actors']
            imdb_score = recs['movies_list'][i]['imdb_score']
            runtime = recs['movies_list'][i]['omdb_runtime']
            rated = recs['movies_list'][i]['rated']
            imdb_url = recs['movies_list'][i]['imdb_url']
            rotten_score = recs['movies_list'][i]['rotten_tomatoes_score']


            movie_dict = {'omdb_title': title, 'omdb_director': director}
            st.session_state.all_movies.append(movie_dict)





            st.write(f' <p style="font-size: 0.9rem;height: 50px;display: flex;align-items: end;font-weight: 600;"> {title} </p>',unsafe_allow_html=True)
            cols[i].image(poster, use_column_width="always")
            
            movie_string = "movie_" + str(i+1)

            with st.expander("More details"):
                st.write(f' <p style="font-size:0.75rem"> <b>Plot:</b> {plot} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>Runtime:</b> {runtime} minutes</p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>Rated:</b> {rated} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>IMDB Score:</b> {imdb_score} </p>',unsafe_allow_html=True)
                if rotten_score:
                    st.write(f' <p style="font-size:0.75rem"> <b>Rotten Tomatoes Score:</b> {int(rotten_score)}% </p>',unsafe_allow_html=True)
                else:
                    st.write(f' <p style="font-size:0.75rem"> <b>Rotten Tomatoes Score:</b> Not Available </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>Genres:</b> {genres} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>Directed by:</b> {director} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> <b>Leading Actors:</b> {actors} </p>',unsafe_allow_html=True)
                st.link_button("Go to IMDB Page →", imdb_url)


    st.write(f'<br>',unsafe_allow_html=True)

    if len(recs["spotify_information"]) > 0:
        counter = 0

        with st.expander("See how we generated your recommendations"):


            num_clusters = len(recs["spotify_information"])

            if num_clusters == 1:
                st.write(f' <p style="font-size:1rem"> We identified 1 taste cluster in your playlist. </p>',unsafe_allow_html=True)
            else:
                st.write(f' <p style="font-size:1rem"> We identified {num_clusters} taste clusters in your playlist. Next, we extracted the mood and music characteristics for each cluster, and then found the movies that were the best match for your mood and taste!</p>',unsafe_allow_html=True)


            cols = st.columns(num_clusters)

            
            for x in recs["spotify_information"]:
                with cols[counter]:


                    mood_vector = recs["spotify_information"][x]['mood_vector']
                    danceability = recs["spotify_information"][x]['danceability']
                    acousticness = recs["spotify_information"][x]['acousticness']
                    energy = recs["spotify_information"][x]['energy']
                    instrumentalness = recs["spotify_information"][x]['instrumentalness']
                    liveness = recs["spotify_information"][x]['liveness']
                    valence = recs["spotify_information"][x]['valence']
                    loudness = recs["spotify_information"][x]['loudness']
                    speechiness = recs["spotify_information"][x]['speechiness']
                    tempo = recs["spotify_information"][x]['tempo']

                    st.write(f' <p style="font-size: 1rem;font-weight: 600;background-color: rgb(240, 242, 246);text-align: center;padding: 5px;border: 1px solid gray;"> Cluster #{counter+1} </p>',unsafe_allow_html=True)

                    st.write(f' <p style="font-size: 0.9rem;font-weight: 600;"> Mood Breakdown: </p>',unsafe_allow_html=True)
                    st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Happy: {str(round(mood_vector[0]*100.00, 2))}% </p>',unsafe_allow_html=True)
                    st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Sad: {str(round(mood_vector[1]*100.00, 2))}%  </p>',unsafe_allow_html=True)
                    st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Energetic: {str(round(mood_vector[2]*100.00, 2))}%  </p>',unsafe_allow_html=True)
                    st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Calm: {str(round(mood_vector[3]*100.00, 2))}%  </p>',unsafe_allow_html=True)

                    st.write(f' <p style="font-size: 0.9rem;padding-top: 20px;font-weight: 600;"> Spotify Stats: </p>',unsafe_allow_html=True)
                    if danceability < 0.3:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Low Danceability </p>',unsafe_allow_html=True)
                    elif danceability < 0.5:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-Low Danceability </p>',unsafe_allow_html=True)
                    elif danceability < 0.7:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-High Danceability </p>',unsafe_allow_html=True)
                    else:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> High Danceability </p>',unsafe_allow_html=True)

                    if energy < 0.3:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Low Energy </p>',unsafe_allow_html=True)
                    elif energy < 0.5:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-Low Energy </p>',unsafe_allow_html=True)
                    elif energy < 0.7:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-High Energy </p>',unsafe_allow_html=True)
                    else:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> High Energy </p>',unsafe_allow_html=True)


                    if tempo < 0.3:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Low Tempo </p>',unsafe_allow_html=True)
                    elif tempo < 0.5:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-Low Tempo </p>',unsafe_allow_html=True)
                    elif tempo < 0.7:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-High Tempo </p>',unsafe_allow_html=True)
                    else:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> High Tempo </p>',unsafe_allow_html=True)


                    if valence < 0.3:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Low Valence </p>',unsafe_allow_html=True)
                    elif valence < 0.5:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-Low Valence </p>',unsafe_allow_html=True)
                    elif valence < 0.7:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> Medium-High Valence </p>',unsafe_allow_html=True)
                    else:
                        st.write(f' <p style="font-size: 0.9rem;padding-left: 20px"> High Valence </p>',unsafe_allow_html=True)
                
                counter = counter + 1

            st.write(f' <p style="font-size:0.85rem;padding-top:20px;"> MovieMood strictly adheres to a data minimization approach. Only essential listening data is collected to perform the mood-based inference and provide relevant movie recommendations. Moreover, this data is not stored beyond the active session, ensuring that users\' personal information is not retained longer than necessary. Once the session ends, all collected data is promptly discarded, maintaining user privacy and reducing potential data-related risks. </p>',unsafe_allow_html=True)



    else:

        st.write("Sorry, we couldn't find any movies! Adjust your filters and try again for better results.")












