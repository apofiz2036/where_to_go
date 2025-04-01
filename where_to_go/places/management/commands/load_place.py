from django.core.management.base import BaseCommand
from places.models import Place, Image  
import requests
from django.core.files.base import ContentFile
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Загружает все локации из папки с JSON-файлами '

    def add_arguments(self, parser):
        parser.add_argument('github_folder_url', type=str)

    def handle(self, *args, **options):
        folder_url = options['github_folder_url']

        response = requests.get(folder_url)
        response.raise_for_status()
        files = response.json()

        for file_info in files:
            if not file_info['name'].endswith('.json'):
                continue

            json_url = file_info['download_url']
            self.stdout.write(f'Загружаем {json_url}...')

            place_data = requests.get(json_url).json()

            place, created = Place.objects.get_or_create(
                title=place_data['title'],
                defaults={
                    'short_description': place_data['description_short'],
                    'long_description': place_data['description_long'],
                    'lng': float(place_data['coordinates']['lng']),
                    'lat': float(place_data['coordinates']['lat']),
                }
            )
            if not created:
                place.images.all().delete()

            for order, img_url in enumerate(place_data['imgs'], start=1):
                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()

                    img_name = urlparse(img_url).path.split('/')[-1]

                    img = Image(
                        place=place,
                        title=f'{place.title} - фото {order}',
                        order=order
                    )
                    img.image.save(
                        img_name,
                        ContentFile(img_response.content),
                        save=True
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка загрузки картинки {img_url}: {e}'))
                finally:
                    img_response.close()

            self.stdout.write(self.style.SUCCESS(
                f'Успешно: {place.title} | Картинок: {len(place_data['imgs'])}'
            ))
