from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','traveler','country','city','notes', 'created_at', 'updated_at')
        model = Trip