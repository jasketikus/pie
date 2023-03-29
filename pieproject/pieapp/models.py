from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

class Characteristic(models.Model):
    name = models.CharField(max_length=30)
    is_published = models.BooleanField(default=False, verbose_name='Published')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    rating = models.IntegerField()
