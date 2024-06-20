from rest_framework.views import APIView
from seller_auth.models import SellerUser
from seller_auth.serializers import UserSerializer
from rest_framework.response import Response


class RegisterView(APIView):
    """
    Registraion API View
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
