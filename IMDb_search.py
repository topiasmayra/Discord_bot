from imdb import Cinemagoer
import pandas as pd

ia = Cinemagoer()

def my_search_function(personname):
    director = ia.search_person(personname)[0]
    director_movies = ia.get_person_filmography(director.personID)

    print(director_movies)

    actor = ia.search_person(personname)[0]
    actor_movies = ia.get_person_filmography(actor.personID)

    # Extracting the filmography
    filmography_director = director_movies.get('data', {}).get('filmography', {}).get('director', [])
    filmography_actor = actor_movies.get('data', {}).get('filmography', {}).get('actor', [])

    # Extracting only the titles
    titles_director = [movie['title'] for movie in filmography_director]
    titles_actor = [movie['title'] for movie in filmography_actor]

    # Creating a DataFrame from the titles
    df = pd.DataFrame({'Title': titles_director + titles_actor})

    return df
