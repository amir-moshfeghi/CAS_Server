import uuid
import jwt
#from api.models import UserModel
# from api.base.serializers.userSerializer import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from api.base.serializers.userSerializer import UserSerializer
from api.base.views.Response import Response
from api.models import UserModel


class UserView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        return None
        # try:
        #     return UserModel.objects.get(pk=pk)
        # except UserModel.DoesNotExist:
        #     raise Http404

    # def get(self, request, pk, format=None):
    #
    #     def login_jwt_check(request):
    #         user = self.get_object(pk)
    #         username = user.username
    #         password = user.password
    #         user = authenticate(username=username, password=password)
    #         if user is None:
    #             return Response(json.dumps({'Error': "User Not Found"}), status=status.HTTP_200_OK, data='',description='',code=''
    #                            )
    #         else:
    #             payload = {
    #                 'id': user.id,
    #                 'email': user.email,
    #             }
    #             jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    #             jwt_token['token'] = jwt_token['token'].decode('utf-8')
    #             user.guid = str(uuid.uuid4())
    #             user.save()
    #             return Response(json.dumps(jwt_token),status=status.HTTP_200_OK, data='',description='',code='')
    #
    #
    #
    #
    #
    #
    #     # TODO : check token else return not found
    #     # TODO : if for pass uuid
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    def post(self, request):
        user = UserSerializer(data=request.data)

        if user.is_valid():

            user.save()
            print(user.data)
            # users = UserModel.objects.all()
            # userxxxx = UserSerializer(users,many=True)
            return Response(data={'user_name':user.data.get('username'),'user_id':user.data.get('id')}, status=status.HTTP_200_OK, message='ok',data_status='200')
        return Response(data=user.data, status=status.HTTP_424_FAILED_DEPENDENCY, message='your data is not valid',data_status='300')

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        if user is True:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
            jwt_token['token'] = jwt_token['token'].decode('utf-8')
            user.guid = str(uuid.uuid4())
            user.save()
            return Response(status=status.HTTP_200_OK, data='',)

        # user = UserSerializer(user, data=request.data)
        # if user.is_valid():
        #     user.save()
        #     return Response(data=user.data)
        # return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)

