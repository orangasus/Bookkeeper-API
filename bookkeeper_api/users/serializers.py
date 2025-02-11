from django.contrib.auth.models import User
from rest_framework import serializers
from .models import OrdinaryUser

class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrdinaryUserSerializer(serializers.ModelSerializer):
    user = DjangoUserSerializer()

    class Meta:
        model = OrdinaryUser
        fields = '__all__'