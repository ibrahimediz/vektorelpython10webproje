from django.urls import path
from . import views


urlpatterns = [
    path('',views.Listele,name="BlogListele"),
    path('<int:pk>/',views.gonderiDetay,name="gDetay"),
    path('yeni/',views.yeniGonderi,name="gYeni"),
    path('duzenle/<int:pk>',views.gonderiDuzenle,name="gDuzenle"),
]


