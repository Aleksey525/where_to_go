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
- `STATIC_URL` — STATIC_URL
- `MEDIA_URL` — MEDIA_URL
- `HOST` — хост проекта
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
  После найти существующую локацию, введя название в поле для поиска и отредактировать ее. Или создать новую.
#####
* Для автоматического заполнения базы даных интегрирована команда `load_place`.  
  Пример запуска команды:  
  ```
  python manage.py load_place http://адрес/файла.json
  ```  
  json-файлы с мета-данными локаций находятся в репозитории [where-to-go-places](https://github.com/devmanorg/where-to-go-places)  
  Образец json-файла с локацией:  
  ```
  {
      "title": "Антикафе Bizone",
      "imgs": [
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
          "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
      ],
      "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
      "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, 
  вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал 
  для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному 
  клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». 
  Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" 
  href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
      "coordinates": {
          "lng": "37.50169",
          "lat": "55.816591"
      }
  }
   ```
  
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman.org](https://dvmn.org).