from django.core.management.base import BaseCommand, CommandError
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loads a location from a link'

    def add_arguments(self, parser):
        parser.add_argument('place_url', nargs='+')

    def handle(self, *args, **options):
        for url in options['place_url']:
            response = requests.get(url).json()
            try:
                place, is_created = Place.objects.get_or_create(
                    title=response['title'],
                    description_short=response['description_short'],
                    description_long=response['description_long'],
                    lat=response['coordinates']['lat'],
                    lng=response['coordinates']['lng'],
                )

                for ind, img_url in enumerate(response['imgs'], start=1):
                    image = place.images.get_or_create(position=ind)
                    image[0].save_img_from_url(img_url)

            except Place.MultipleObjectsReturned:
                raise CommandError(f'Place object has more than one object')

            except Image.MultipleObjectsReturned:
                raise CommandError(f'Image object has more than one object')