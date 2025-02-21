from rest_framework import serializers
from django.contrib.auth.models import User


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5000)


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create_user(
            username=username, email=username, password=password
        )
        return user
