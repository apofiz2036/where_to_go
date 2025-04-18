from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.urls import reverse

from .models import Place


def place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
    )

    imgs = [image.image.url for image in place.images.all()]

    place_data = {
        'title': place.title,
        'imgs': imgs,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(place_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def index(request):
    places = Place.objects.all()
    features = []

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_details', args=[place.id])
            }
        }
        features.append(feature)

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    return render(request, 'index.html', {'geojson': geojson})
