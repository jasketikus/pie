from django.contrib import admin
from django.urls import path

from pieapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', ProfilePage.as_view(), name='profile'),
    path('addchar/', AddCharacteristic.as_view(), name='addchar'),
    path('characteristic/<int:pk>/', CharacteristicDetailView.as_view(), name='characteristic_detail'),
    path('characteristic/<int:pk>/update', CharacteristicUpdateView.as_view(), name='characteristic_update'),
    path('characteristic/<int:pk>/delete', CharacteristicDeleteView.as_view(), name='characteristic_delete'),
]
