
# Create your views here.


from django.http import HttpResponse


from django.shortcuts import render

# Create your views here.
from .models import Movie

from django.http import HttpResponse

'''def index(request):

  text = """<h1>Anit Bijalasmi</h1>"""
  return HttpResponse(text)'''


def index(request):
    all_movies = Movie.objects.all()

    for b in all_movies:
        url = '/Home/' + str(b.id) + '/'

        html = '<a href =" ' + url + ' ">' + b.actor + '</a>'

    return HttpResponse(html)


def detail(request,lacebook_id):

    return HttpResponse("<h1> welcome to INDIA:" + str(lacebook_id) + "</h1>")






