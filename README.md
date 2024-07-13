# Сайт с интерактивной картой Москвы

![screenshot](https://github.com/Aleksey525/where_to_go/blob/master/site_screenshot.jpg)
### Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```

pip install -r requirements.txt

```

Создайть БД:
```
python manage.py migrate
```
Создайть суперпользователя:
```
python manage.py createsuperuser
```
Запустить разработческий сервер:
```
python manage.py runserver
```
```
System check identified no issues (0 silenced).
July 13, 2024 - 21:19:53
Django version 4.2.6, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/      
Quit the server with CTRL-BREAK.
```
### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корневом каталоге проекта и 
запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `SECRET_KEY` — секретный ключ проекта
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `ALLOWED_HOSTS` — см. [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `STATIC_URL` — секретный ключ проекта
- `MEDIA_URL` — секретный ключ проекта
- `DETAILS_URL` — секретный ключ проекта
### Сценарии использования
* Проверить работу сайта можно перейдя по ссылке [where_to_go](https://alekseitol.pythonanywhere.com/).  
  Перейти в админ панель для добавления новой локации, координат, описания и фотографий можно по ссылке 
  [admin_panel](https://alekseitol.pythonanywhere.com/admin)  
  `login: alex`  
  `password: 123`
#####
* Проверить работу сайта на смартфоне можно по тем же ссылкам.
#####
* Чтобы наполнить сайт контентом, нужно перейти по ссылке [admin_panel_places](https://alekseitol.pythonanywhere.com/admin/places/place/).  
  Далее можно найти существующую локацию, введя название в поле для поиска и отредактировать ее. Или создать новую.
#####
* Для автоматического заполнения базы даных интегрирована команда `load_place`.  
  Пример запуска команды:  
  ```
  python manage.py load_place http://адрес/файла.json
  ```  
  json файлы с мета-данными локации находятся в репозитории [where-to-go-places](https://github.com/devmanorg/where-to-go-places)
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman.org](https://dvmn.org).