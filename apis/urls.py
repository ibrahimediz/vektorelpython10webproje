from django.urls import path
from .views import TodoViewSet

# from .views import ListBlog,DetayBlog
# urlpatterns = [
#     path('',ListBlog.as_view()),
#     path('<int:pk>/',DetayBlog.as_view()),

# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',TodoViewSet,base_name='todo')
urlpatterns = router.urls
