from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    yazar = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olusturma_zaman = models.DateTimeField(default=timezone.now)
    yayim_zaman = models.DateTimeField(null=True,blank=True)


    def yayimla(self):
        self.yayim_zaman = timezone.now


    def __str__(self):
        return self.baslik
    


