from django.contrib import admin
from django.urls import path

from pieapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
]
