from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import OrdinaryUser
from .serializers import OrdinaryUserSerializer


class UsersViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='create_user')
    def create_user(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
        }

        serializer = OrdinaryUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='get_all_users')
    def get_all_users(self, request, *args, **kwargs):
        users = OrdinaryUser.objects.all()
        serializer = OrdinaryUserSerializer(instance=users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
