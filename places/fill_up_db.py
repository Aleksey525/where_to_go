import sys
import time

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from urllib.parse import urlsplit, unquote

import os
import requests

from .models import Place, Image


RECONNECTION_DELAY = 30


def get_file_name(file_link):
    splited_link = urlsplit(file_link)
    file_path = unquote(splited_link.path)
    splited_file_path = os.path.split(file_path)
    file_name = splited_file_path[1]
    return file_name


def load_image_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    file_name = get_file_name(url)
    image_data = ContentFile(response.content)
    image_file = default_storage.save(file_name, image_data)
    return image_file


def main(url):
    response = requests.get(url)
    response.raise_for_status()
    place = response.json()
    title = place['title']
    long_description = place['description_long']
    short_description = place['description_short']
    lat = place['coordinates']['lat']
    lng = place['coordinates']['lng']
    images = place['imgs']

    try:
        place_obj, created = Place.objects.get_or_create(
            title=title,
            defaults={'long_description': long_description,
                      'short_description': short_description,
                      'lat': lat,
                      'lng': lng
                      }
        )
    except MultipleObjectsReturned:
        sys.stderr.write('Найдено несколько одинаковых записей\n')
    except ObjectDoesNotExist:
        sys.stderr.write('Запись не существует\n')

    for position, image_url in enumerate(images):
        try:
            image_file = load_image_from_url(image_url)
            Image.objects.create(img=image_file, place=place_obj, position=position + 1)
        except requests.exceptions.HTTPError:
            sys.stderr.write('Ошибка HTTP\n')
            continue
        except requests.exceptions.ConnectionError:
            sys.stderr.write('Ошибка подключения\n')
            time.sleep(RECONNECTION_DELAY)
    else:
        sys.stderr.write('Локация скачана\n')









