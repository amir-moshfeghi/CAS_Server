from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.views import APIView

from api.base.views.Response import Response
from api.base.views.userBackend import *
#from api.models import UserModel


class AuthTokenView(APIView):

    def post(self, request):
        username =request.data.get('username')
        password =request.data.get('password')
        # username = request.POST['username']
        # password = request.POST['password']
        # username=get_user_model().objects.get('username')
        # password=get_user_model().objects.get('password')


        print (username)
        print (password)
        # print (request.data.get('password')
        user = authenticate(username=username,password=password)
        print(user)

        # TODO : auth with default django function
        if user is not None:
            return Response(data=user.username,status=status.HTTP_200_OK,message='',data_status='ok')
        else:
            return Response(data='',status=status.HTTP_400_BAD_REQUEST,message='',data_status='')

