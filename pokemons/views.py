from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


import requests
import json

from pokemons.models import Pokemon
from django.views.generic import DetailView, ListView
from django.http import Http404

BASE_URL = 'https://pokeapi.co'

def query_pokeapi(resource_uri):
    api_url = f'{BASE_URL}{resource_uri}'
    request = requests.get(api_url)
    json_request = request.json()
    return json_request


class IndexView(ListView):
    model = Pokemon


class PokemonView(DetailView):
    model = Pokemon
    context_object_name = 'pokemon'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get("name")
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        try:
            pokemon_url = '/api/v2/pokemon/{0}/'.format(pk)
            pokemon = query_pokeapi(pokemon_url)

            if pokemon:

                t_pokemon, created = queryset.get_or_create(
                    name=pokemon['name'],
                    base_experience=pokemon['base_experience'],
                    image_url=pokemon['sprites']['front_default']
                )
                return t_pokemon
        except queryset.model.DoesNotExist:
            raise Http404(_("Not found"))
