from rest_framework import serializers
from django.contrib.auth import get_user_model


User=get_user_model()

class CreateSuperUserSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()



    def validate(self, attrs):
        super().validate(attrs)
        if(attrs['password']!=attrs['confirm_password']):
            raise serializers.ValidationError("Wrong password")


        user=User.objects.create_superuser(
            username=attrs['username'],
            password=attrs['password'],
            first_name=attrs['first_name'],
            last_name=attrs['last_name']
            )

        
        
        return attrs

class LoginUserSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


    def validate(self, attrs):
        return super().validate(attrs)