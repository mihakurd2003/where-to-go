from django.core.management.base import BaseCommand, CommandError
import requests
from urllib.parse import urlparse
from places.models import Place, Image
from django.core.files.base import ContentFile


def save_image(place: Place, image_content: bytes, position: int, name: str):
    content_file = ContentFile(image_content, name=name)
    image = Image.objects.create(place=place, image=content_file, position=position)

    return image


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
                    image_content = requests.get(img_url).content
                    img_name = str(urlparse(img_url).path.split('/')[-1])
                    print(img_name, img_url)
                    save_image(place, image_content, ind, img_name)

            except Place.MultipleObjectsReturned:
                raise CommandError(f'Place object has more than one object')

            except Image.MultipleObjectsReturned:
                raise CommandError(f'Image object has more than one object')