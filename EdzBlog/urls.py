from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.gonderilistele,name="gonderilist"),
    path('',views.anasayfa,name="gonderilist"),
]