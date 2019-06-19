from rest_framework import generics
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer
from .models import user_profile

# Seriliazer for user profile


class user_profile_serializer(ModelSerializer):
    class Meta:
        model = user_profile
        fields = ('id', 'username', 'name', 'date_of_birth', 'password')
        #  To make password write only
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = user_profile(
            username=validated_data['username'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
