from imdb import Cinemagoer
import pandas as pd
import numpy as np

ia = Cinemagoer()

personname = input("Syötä ohjaajan tai näyttelijän nimi: ")
director = ia.search_person(personname)
movies1 = ia.get_person_filmography(director[0].personID)



filmography = movies1.get('data', {}).get('filmography', {}).get('director', [])

#checking if the filmography is movie or tv series
kind = [movie['kind'] for movie in filmography ]

# Extracting only the titles
titles = [movie['title'] for movie in filmography ]

# Creating a DataFrame from the titles
df = pd.DataFrame({'Title': titles})



# Removing duplicates
df = df.drop_duplicates(subset=['Title'])

print(df)

