from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.http import JsonResponse
from django.urls import reverse
from .models import Place
import json


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
    imgs = [image.image.url for image in images]

    place_data = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(place_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def index(request):
    places = Place.objects.all()
    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_details', args=[place.id])
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', {'geojson': geojson})
