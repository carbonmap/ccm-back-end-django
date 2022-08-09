from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import ReportingEntity, ReportingEntityAddress, UserToEntity


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


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
        fields = ('token', 'username', 'password')

class ReportingEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportingEntity
        fields = ('name', 'id')

class ReportingEntityAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportingEntityAddress
        fields = ('id','street_address', 'address_locality', 'address_region', 'postal_code', 'address_country')

class UserToEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserToEntity
        fields = ('user_id','entity_id')