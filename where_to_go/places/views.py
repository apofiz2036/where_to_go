from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from .models import Place
import json


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    imgs = []
    if place.first_image:
        imgs.append(place.first_image.image.url)

    for image in place.second_image.all():
        imgs.append(image.image.url)

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

    print(json.dumps(geojson, ensure_ascii=False, indent=4))

    geojson_str = json.dumps(geojson, ensure_ascii=False, indent=4)
    return render(request, 'index.html', {'geojson': geojson_str})
