from rest_framework import serializers
from seller_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    serializer class for User model
    """

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
