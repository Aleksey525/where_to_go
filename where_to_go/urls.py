from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places.views import index_page, places_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('places/<int:place_id>/', places_page, name='places_page'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)