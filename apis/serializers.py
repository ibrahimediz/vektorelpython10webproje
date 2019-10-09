from rest_framework import serializers
from todo import models



class todoSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','baslik','detay')
        model = models.todoModel