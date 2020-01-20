from rest_framework import serializers

# from api.models import UserModel


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     nick_name = serializers.CharField()
#     password = serializers.CharField()
#     email = serializers.CharField()
#     mobile = serializers.IntegerField()
#     address = serializers.CharField()
#     # photo = serializers.ImageField()
#     type = serializers.CharField()
#     # last_login_date = serializers.DateTimeField(default=datetime.now())
#     # last_edit = serializers.DateTimeField()
from api.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = "__all__"
        fields = ['username','id']

    # def create(self, validated_data):
    #     """
    #     Create and return a new `user` instance, given the validated data.
    #     """
    #     return UserModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `user` instance, given the validated data.
    #     """
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.nick_name = validated_data.get('nick_name', instance.nick_name)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.mobile = validated_data.get('mobile', instance.mobile)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.photo = validated_data.get('photo', instance.photo)
    #     instance.type = validated_data.get('type', instance.type)
    #     instance.last_login_date = validated_data.get('last_login_date', instance.last_login_date)
    #     instance.save()
    #     return instance