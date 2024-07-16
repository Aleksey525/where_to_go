from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from environs import Env
from django.urls import reverse


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
            'detailsUrl': reverse('places_page', args=[place.pk])
        }
    }


def index_page(request):
    places = Place.objects.all()
    features = [serialize_place(place) for place in places]
    place_serialize = {
        'type': 'FeatureCollection',
        'features': features
    }
    context = {'places_geo': place_serialize}
    return render(request, 'index.html', context=context)


def places_page(request, place_id=None):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=place_id)
    place_serialize = {
        'title': place.title,
        'imgs': [image.img.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_serialize, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
