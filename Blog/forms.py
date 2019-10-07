from django import forms

from .models import Gonderi

class GonderiForm(forms.ModelForm):

    class Meta:
        model = Gonderi
        fields = ('yazar','baslik', 'yazi','olus_zaman','hashtag','cover')