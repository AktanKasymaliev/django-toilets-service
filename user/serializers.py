from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        if len(password) < 6:
            raise serializers.ValidationError({'password':'Your password is too short'})
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'Email address must be unique'})
        return attrs

    def create(self, validated_data):
        if validated_data():
            user = User.objects.create_user(**validated_data)
            return user
        else:
            return serializers.ValidationError({'validation':'Entered data is not valide'})