from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirmation')

    def validate(self, attrs):
        password2 = attrs.pop('password_confirmation')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Password didnt match!')

        if not attrs['first_name'].istitle():
            raise serializers.ValidationError('Name must start with uppercase letter!')

        return attrs

    def validate_password(self, value):
        try:
            validate_password(value)

        except serializers.ValidationError as error:
            raise serializers.ValidationError(str(error))

        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
