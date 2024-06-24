from rest_framework import serializers
from seller_auth.models import SellerUser
from Ailaysa_app.serializers import PublisherSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    serializer class for User model
    """
    publisher = PublisherSerializer(many=True)

    class Meta:
        model = SellerUser
        fields = '__all__'

    def create(self, validated_data):
        user = SellerUser.objects.create(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
