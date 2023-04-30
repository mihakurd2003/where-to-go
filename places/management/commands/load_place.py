from django.core.management.base import BaseCommand, CommandError
import requests
from urllib.parse import urlparse
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Loads a location from a link'

    @staticmethod
    def get_place(url):
        response = requests.get(url)
        response.raise_for_status()

        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])

        return decoded_response

    @staticmethod
    def get_image(url):
        image_response = requests.get(url)
        image_response.raise_for_status()
        img_name = str(urlparse(url).path.split('/')[-1])

        return image_response, img_name

    @staticmethod
    def save_image(place: Place, image_content: bytes, position: int, name: str):
        content_file = ContentFile(image_content, name=name)
        image = Image.objects.create(place=place, image=content_file, position=position)

        return image

    def add_arguments(self, parser):
        parser.add_argument('place_url', nargs='+')

    def handle(self, *args, **options):
        for url in options['place_url']:
            try:
                decoded_response = Command.get_place(url)

                place, is_created = Place.objects.get_or_create(
                    title=decoded_response['title'],
                    description_short=decoded_response.get('description_short', ''),
                    description_long=decoded_response.get('description_long', ''),
                    lat=decoded_response['coordinates']['lat'],
                    lng=decoded_response['coordinates']['lng'],
                )

                image_urls = decoded_response.get('imgs', []) if is_created else []
                for ind, img_url in enumerate(image_urls, start=1):
                    image_response, img_name = Command.get_image(img_url)
                    Command.save_image(place, image_response.content, ind, img_name)

            except Place.MultipleObjectsReturned:
                raise CommandError('Place object has more than one object')

            except Image.MultipleObjectsReturned:
                raise CommandError('Image object has more than one object')
