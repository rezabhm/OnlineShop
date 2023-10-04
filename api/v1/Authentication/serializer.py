import uuid

from rest_framework import serializers
from django.contrib.auth.models import User
from App_05__Product import models
from App_04__Core import models as core_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:

        model = User
        fields = [

                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password',
                    'confirm_password',

        ]

    def validate(self, attrs):
        """

            validate password with confirm password

        """

        if str(attrs['password']) != str(attrs['confirm_password']):
            raise serializers.ValidationError({'password': "password and confirm password didn't match"})

        return attrs

    def create(self, validated_data):

        """

            create user objects

        """

        # create user
        user = User.objects.create(

            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

        )

        user.set_password(validated_data['password'])

        user.save()

        # create user branch
        user_obj = core_model.UserInf(

            id=str(uuid.uuid4().int),
            user_type='customer',
            user=user

        )

        user_obj.save()

        return user
