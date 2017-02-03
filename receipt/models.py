from django.db import models
from django.contrib.auth.models import User


class Paragon(models.Model):
    image = models.FileField()
    image_data = models.TextField(null=True, blank=True, default='Processing image... Refresh to check for results. If that doesnt help please wait or do something else one the website')
    user1 = models.ForeignKey(User, blank=True, null=True)

def __str__(self):
        return str(self.image)


class ParagonItems(models.Model):
    id_paragonu =models.ForeignKey(Paragon, blank=True, null=True)  
    cena = models.CharField(max_length=120, null=True, blank=True)
    produkt = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return (self.produkt)

