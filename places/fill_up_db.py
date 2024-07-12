import os
import requests
from .models import Place, Image
from urllib.parse import urlsplit, unquote
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def get_file_name(file_link):
    splited_link = urlsplit(file_link)
    file_path = unquote(splited_link.path)
    splited_file_path = os.path.split(file_path)
    file_name = splited_file_path[1]
    return file_name


def load_image_from_url(url):
    response = requests.get(url)
    file_name = get_file_name(url)
    image_data = ContentFile(response.content)
    image_file = default_storage.save(file_name, image_data)
    return image_file


def main(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    title = data['title']
    description_long = data['description_long']
    description_short = data['description_short']
    lat = data['coordinates']['lat']
    lng = data['coordinates']['lng']
    images = data['imgs']

    Place.objects.get_or_create(
        title=title,
        description_long=description_long,
        description_short=description_short,
        lat=lat,
        lng=lng
    )

    place = Place.objects.get(title=title)
    for position, image_url in enumerate(images):
        image_file = load_image_from_url(image_url)
        image_model = Image(title=title, img=image_file, place=place, position=position + 1)
        image_model.save()



