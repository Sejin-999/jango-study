from rest_framework.serializers import ModelSerializer
from .models import user

class TestUserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'