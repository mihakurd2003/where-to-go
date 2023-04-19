import json
from django.shortcuts import render
from .models import Place


def show(request):
    places = Place.objects.prefetch_related('images')

    geojson_positions = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [37.62, 55.793676]
                },
                'properties': {
                    'title': 'Легенды Москвы',
                    'placeId': 'moscow_legends',
                    'detailsUrl': "static/places/moscow_legends.json",
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [37.64, 55.753676]
                },
                'properties': {
                    'title': 'Крыши24.рф',
                    'placeId': 'roofs24',
                    'detailsUrl': "/static/places/roofs24.json",
                }
            }
        ],
    }
    # for place in places:
    #     geo_place = {
    #         'title': place.title,
    #         'imgs': [obj.image.url for obj in place.images.all()],
    #         'description_short': place.description_short,
    #         'description_long': place.description_long,
    #         'placeId': 'moscow_legends',
    #         'coordinates': {
    #             'lng': place.lng,
    #             'lat': place.lat,
    #         },
    #     }
    #
    #     geojson_positions['features'].append({
    #         'type': 'Feature',
    #         'geometry': {
    #             'type': 'Point',
    #             'coordinates': [place.lng, place.lat],
    #         },
    #         'properties': {
    #             'title': place.title,
    #             'placeId': geo_place["placeId"],
    #             'detailsUrl': f'/static/places/{geo_place["placeId"]}.json',
    #         },
    #     })

    return render(request, 'index.html', {'places': geojson_positions})
