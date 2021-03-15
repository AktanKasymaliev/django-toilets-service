from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    