from rest_framework.serializers import ModelSerializer
from .models import Fruit

class TestFruitSerializer(ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'