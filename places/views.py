from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import Place


def show_places(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_details', args=[place.id]),
            },
        })

    geojson_positions = {
        'type': 'FeatureCollection',
        'features': features,
    }

    return render(request, 'index.html', {'places': geojson_positions})


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    serialized_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        },
    }

    return JsonResponse(serialized_place, json_dumps_params={'ensure_ascii': False, 'indent': 4})
