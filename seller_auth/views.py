from seller_auth.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError


class RegisterView(APIView):
    """
    Registration API View
    """
    @staticmethod
    def post(request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    Logout API View
    """
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        token = RefreshToken(request.data['refresh'])
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
