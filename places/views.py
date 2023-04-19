from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Place


def show_places(request):
    places = Place.objects.prefetch_related('images')

    geojson_positions = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in places:
        geojson_positions['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': '',
            },
        })

    return render(request, 'index.html', {'places': geojson_positions})


def place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)

    json_place = {
        'title': place.title,
        'imgs': [obj.image.url for obj in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        },
    }

    return JsonResponse(json_place, json_dumps_params={'ensure_ascii': False, 'indent': 4})
