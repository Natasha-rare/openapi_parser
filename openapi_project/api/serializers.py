# serializers.py
from rest_framework import serializers
from .models import Cinemas

class CinemasSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cinemas
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        return representation