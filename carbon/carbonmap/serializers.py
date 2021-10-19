from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from django.core.validators import EmailValidator, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'email'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate_email(self, value):
        """Validate that a username is email like."""
        _validate_email = EmailValidator()
        try:
            _validate_email(value=['email'])
        except ValidationError:
            raise ValidationError('Enter a valid email address.')
        return value

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2' )

    def validate(self, attrs):
        print('VALIDATING')
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs


    def create(self, validated_data):
        # validated_data.pop('password2')
        # created_user = super().create(validated_data)
        created_user = User.objects.create(
            email=validated_data['email']
        )
        #
        created_user.set_password(validated_data['password'])
        created_user.save()

        return created_user


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'email', 'password')

