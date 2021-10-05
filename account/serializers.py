from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return token
