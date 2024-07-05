
from django.contrib import admin
from django.urls import path
from where_to_go.views import index_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page)
]
