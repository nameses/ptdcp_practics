import requests
from django.http import HttpResponse
from django.shortcuts import render
from movieapp.forms import MovieForm
import config

def recommend_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            min_avg_rating = form.cleaned_data['min_avg_rating']

            url = (
                f'https://api.themoviedb.org/3/discover/movie?api_key={config.api_key}&language=en-US&sort_by=popularity.desc'
                f'&with_genres={genre}&primary_release_year={year}&vote_average.gte={min_avg_rating}')

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                recommended_movie = data.get('results', [])[0]
                return render(request, 'rec_result.html', {'recommended_movie': recommended_movie})
            else:
                return HttpResponse('Error fetching movie recommendation.')
    else:
        form = MovieForm()

    return render(request, 'recommend_movie.html', {'form': form})