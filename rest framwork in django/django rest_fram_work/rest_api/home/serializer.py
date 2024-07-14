from rest_framework import serializers
from .models import todo

class TodoSrializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'