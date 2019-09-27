from django.shortcuts import render
from .forms import IletisimForm

def yenimesaj(request):
    form = IletisimForm()
    return render(request,'Iletisim/yeni_mesaj.html',{'form':form})