from rest_framework import serializers
from seller_auth.models import SellerUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerUser
        fields = '__all__'

    def create(self, validated_data):
        user = SellerUser.objects.create(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
