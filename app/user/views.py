from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions
from user.serializers import UsersSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken


class ListUsersView(generics.ListAPIView):
    """list all exixting users"""
    serializer_class = UsersSerializer
    queryset = get_user_model().objects.all()


class CreateUsersView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UsersSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage authenticated user model"""
    serializer_class = UsersSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """get and return authenticated user"""
        return self.request.user
