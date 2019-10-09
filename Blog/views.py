from django.shortcuts import render,get_object_or_404,redirect
from .models import Gonderi
from .forms import GonderiForm
from django.contrib.auth.models import User
from django.utils import timezone

def Listele(request):
    gonderi = Gonderi.objects.filter(yazar=request.user).order_by('-id')
    return render(request,"Blog/liste.html",{"gonderiler":gonderi})


def gonderiDetay(request,pk=0):
    gonderi = get_object_or_404(Gonderi,pk=pk)
    return render(request,"Blog/detay.html",{"post":gonderi})


def yeniGonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST,request.FILES)
        if form.is_valid():
            gonderi = form.save(commit=False)
            # ben = User.objects.get(username="admi")
            gonderi.yazar = request.user
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gDetay', pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request,'Blog/yeni.html',{"form":form})



def gonderiDuzenle(request,pk):
    gonderi = get_object_or_404(Gonderi,pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST,instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            # ben = User.objects.get(username="admi")
            gonderi.yazar = request.user
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gDetay', pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request,'Blog/duzenle.html',{"form":form})