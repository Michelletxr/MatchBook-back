from enum import unique
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import User, UserProfileImage

class UserProfileImageSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    url = serializers.CharField(max_length=255, read_only=True)
    delete_hash = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = UserProfileImage
        fields = ['id', 'url', 'delete_hash']

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)
    latitude = serializers.DecimalField(max_digits=12, decimal_places=9, required=True)
    longitude = serializers.DecimalField(max_digits=12, decimal_places=9, required=True)
    profile_image = UserProfileImageSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email']
            )
        ]
    
    def create(self, validated_data):
        password: str = validated_data.get('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)

        instance.save()

        return instance