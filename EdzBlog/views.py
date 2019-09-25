from django.shortcuts import render
from .models import Gonderi


def gonderilistele(request):
    gonderiler = Gonderi.objects.all()
    return render(request,'EdzBlog/gonderiliste.html',{"gonderiler":gonderiler})