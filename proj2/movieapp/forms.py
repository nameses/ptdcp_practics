import requests
from django import forms

import config


def get_tmdb_genres():
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={config.api_key}&language=en-US'
    response = requests.get(url)
    data = response.json()
    genres = [(genre['id'], genre['name']) for genre in data['genres']]
    return genres


class MovieForm(forms.Form):
    year = forms.IntegerField()
    genre = forms.ChoiceField(choices=[(genre_id, genre_name) for genre_id, genre_name in get_tmdb_genres()])
    min_avg_rating = forms.FloatField()
