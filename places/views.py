from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from environs import Env


env = Env()
env.read_env()
HOST = env.str('DETAILS_URL')


def serialize_place(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": f'http://{HOST}/places/{place.pk}/'
        }
    }


def index_page(request):
    places = Place.objects.all()
    features = [serialize_place(place) for place in places]
    place_data = {
        "type": "FeatureCollection",
        "features": features
    }
    context = {'places_geo': place_data}
    return render(request, 'index.html', context=context)


def places_page(request, place_id=None):
    place = get_object_or_404(Place, pk=place_id)
    images = Image.objects.filter(title=place.title)
    place_data = {
        'title': place.title,
        'imgs': [image.img.url for image in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
