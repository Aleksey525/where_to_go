from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place, Image


def serialize_place(place):
    return {
      'title': place.title,
      'imgs': '',
      'short_description': place.description_short,
      'description_long': place.description_long,
      'lat': place.lat,
      'lng': place.lng
    }


def serialize_image(image):
    return {
        'title': image.title,
        'imgs': image.imgs.url
    }


def index_page(request):
    places = Place.objects.all()
    context = {
      'places_geo': {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [places[0].lng, places[0].lat]
              },
              "properties": {
                "title": places[0].title,
                "placeId": "moscow_legends",
                "detailsUrl": ""
              }
            },
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [places[1].lng, places[1].lat]
              },
              "properties": {
                "title": places[1].title,
                "placeId": "roofs24",
                "detailsUrl": ""
              }
            }
          ]
      }
    }
    return render(request, 'index.html', context=context)
