from django.db import models
from django.utils import timezone

class IletisimMod(models.Model):
    Adı = models.CharField(max_length=200)
    Soyadı = models.CharField(max_length=200)
    E_Posta = models.EmailField(max_length=200)
    Mesaj = models.TextField()
    Zaman = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.E_Posta