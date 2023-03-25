from django.contrib import admin
from django.urls import path

from pieapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', ProfilePage.as_view(), name='profile')
]
