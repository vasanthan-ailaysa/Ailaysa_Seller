from rest_framework.views import APIView
from seller_auth.models import SellerUser
from seller_auth.serializers import UserSerializer
from rest_framework.response import Response


"""
Registraion API View
"""
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(SellerUser, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
