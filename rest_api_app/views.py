from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_api_app import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """Test Api Viw"""
    serializer_class = serializers.HelloSerializers
    def get(self, request, format=None):
        an_apiview = "hello this is api"
        return Response({"message": "hello", "an_apiview": an_apiview})


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello this is my name {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


