from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import ConfirmationCode
import random

def gen_code():
    return f"{random.randint(0, 999999):06d}"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id username email password'.split(' ')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()

        code = gen_code()
        ConfirmationCode.objects.create(user=user, code=code)

        print(f"Confirmation code for {user.email}: {code}")

        return user
    
class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        try:
            cc = user.confirmation_code
        except ConfirmationCode.DoesNotExist:
            raise serializers.ValidationError("Confirmation code not found")
        
        if cc.code != code:
            raise serializers.ValidationError("Invalid code")
        
        attrs['user'] = user
        attrs['confirmation'] = cc
        return attrs

class AuthValidationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists')