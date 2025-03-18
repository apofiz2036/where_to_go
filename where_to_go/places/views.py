from django.shortcuts import render
from django.templatetags.static import static
from django.http import JsonResponse
from .models import Place
import json
import os


def load_json():
    places = []
    static_dir = r'C:\Users\Apofiz\Desktop\study\django\where_to_go\where_to_go\static\places'

    for filename in os.listdir(static_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(static_dir, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                place_data = json.load(file)
                place_data["placeId"] = os.path.splitext(filename)[0]
                places.append(place_data)

    return places


def index(request):
    places = load_json()
    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place["coordinates"]["lng"], place["coordinates"]["lat"]]
            },
            "properties": {
                "title": place["title"],
                "placeId": place["placeId"],
                "detailsUrl": static(f'places/{place["placeId"]}.json')
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
