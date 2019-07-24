from rest_framework import serializers
from plants.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        #fields = ('id', 'name', 'email')
        fields = '__all__'