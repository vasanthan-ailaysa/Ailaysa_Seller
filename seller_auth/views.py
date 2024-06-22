from seller_auth.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_205_RESET_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    """
    Registraion API View
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response(status=HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    Logout API View
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=HTTP_400_BAD_REQUEST)
