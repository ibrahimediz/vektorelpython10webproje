from django.db import models

class IletisimMod(models.Model):
    Adı = models.CharField(max_length=200)
    Soyadı = models.CharField(max_length=200)
    E_Posta = models.EmailField(max_length=200)
