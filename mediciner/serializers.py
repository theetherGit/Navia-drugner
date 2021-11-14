from rest_framework import serializers
from .models import DrugList
class DrugListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugList
        fields = '__all__'