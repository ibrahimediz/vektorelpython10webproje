from rest_framework import generics,viewsets

from todo import models
from .serializers import todoSerializer

# class ListBlog(generics.ListCreateAPIView):
#     queryset = models.Gonderi.objects.all()
#     serializer_class = BlogSerializer

# class DetayBlog(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Gonderi.objects.all()
#     serializer_class = BlogSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.todoModel.objects.all()
    serializer_class = todoSerializer