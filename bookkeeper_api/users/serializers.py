from django.contrib.auth.models import User
from rest_framework import serializers

from .models import OrdinaryUser


class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class OrdinaryUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = OrdinaryUser
        fields = '__all__'
        # so json doesn't need to have 'django_user' subdict
        extra_kwargs = {'django_user': {'required': False}}

    def create(self, passed_data):
        username = passed_data.pop('username')
        password = passed_data.pop('password')

        django_user = User.objects.create(username=username)
        django_user.set_password(password)
        django_user.save()

        ordinary_user = OrdinaryUser.objects.create(django_user=django_user, **passed_data)
        ordinary_user.public_username=f'U{ordinary_user.id}'
        ordinary_user.save()
        return ordinary_user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.django_user.username
        return representation
