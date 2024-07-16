from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from environs import Env


env = Env()
env.read_env()
host = env.str('HOST', '127.0.0.1:8000')


def serialize_place(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
        },
        "properties": {
            'title': place.title,
            'placeId': place.pk,
            'detailsUrl': f'http://{host}/places/{place.pk}/'
        }
    }


def index_page(request):
    places = Place.objects.all()
    features = [serialize_place(place) for place in places]
    place_data = {
        'type': 'FeatureCollection',
        'features': features
    }
    context = {'places_geo': place_data}
    return render(request, 'index.html', context=context)


def places_page(request, place_id=None):
    place = get_object_or_404(Place, pk=place_id)
    place_data = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
