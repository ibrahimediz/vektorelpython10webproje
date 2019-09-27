from django import forms

from .models import IletisimMod

class IletisimForm(forms.ModelForm):

    class Meta:
        model = IletisimMod
        fields = ('Adı', 'Soyadı','E_Posta','Mesaj')