from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        write_only = True,
        required = True,
        validators=[UniqueValidator(
            queryset = User.objects.all(),
            message = "A user with that email already exists."
            )]
    )

    class Meta:
        model = User
        fields = ("id", "username", "email" ,"password", "userprofile",)
        read_only_fields = ("username",)
        extra_kwargs = {
            "password": {"write_only":True},
        }

    def create(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        else:

            try:
                user = User.objects.create_user(username=username, email=email, password=password, is_active=False)
            except IntegrityError:
                raise serializers.ValidationError("A user with that email already exists.")
            else:
                send_confrimation_email(email_subject = "Aktywacja konta", 
                                        template_path="account_activation_email.html",
                                        user=user,
                                        email=email)
            return user
