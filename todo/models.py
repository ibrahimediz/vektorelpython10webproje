from django.db import models

class todoModel(models.Model):
    baslik = models.CharField(max_length=200)
    detay = models.CharField(max_length=200)