from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView

from .serializers import RegisterSerializer, UserSerializer

'''
  A class for registering users
'''


class RegisterAPI(APIView):
    def post(self, request, format='json'):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                data = {
                    'token': token.key,
                    'user': {
                        'userId': user.pk,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'username': user.username,
                        'email': user.email,
                        'address1': user.address1,
                        'address2': user.address2,
                        'phone_number': user.phone_number,
                    },
                }
                return JsonResponse({'status': True, 'msg': 'Succesfully created user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Could not create user', 'data': {}}, status=200)


'''
  A class for login user
'''

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user:
                token, create = Token.objects.get_or_create(user=user)
                data = {
                    'token': token.key,
                    'user': {
                        'userId': user.pk,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'username': user.username,
                        'email': user.email,
                        'address1': user.address1,
                        'address2': user.address2,
                        'phone_number': user.phone_number,
                    },
                }
                return JsonResponse({'status': True, 'msg': 'Succesfully logged in user', 'data': data}, status=200)
        return JsonResponse({'status': False, 'msg': 'Username or Password is incorect', 'data': {}}, status=200)


class LogOutAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        return JsonResponse({'status': True, 'msg': 'Successfully logged out'})


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user