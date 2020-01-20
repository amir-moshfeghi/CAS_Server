# # from django.contrib.auth.backends import ModelBackend
# # from django.contrib.auth.models import User
# #
# # from api.models import UserModel
# #
# # class UserBackend(ModelBackend):
# #
# #     def authenticate(self, request, **kwargs):
# #         user_id = kwargs['username']
# #         password = kwargs['password']
# #         try:
# #             user = UserModel.objects.get(user_id=user_id)
# #             if user.userinfo.check_password(password) is True:
# #                 return user.userinfo
# #         except UserModel.DoesNotExist:
# #             pass
# #
# # from django.contrib.auth.backends import ModelBackend
# # from django.contrib.auth.models import User
# #
# #
# #
# #
# # class CustomerBackend(ModelBackend):
# #
# #     def authenticate(self, request, **kwargs):
# #         user_id = kwargs['username']
# #         password = kwargs['password']
# #         print (password)
# #         try:
# #             user = User.objects.get(username=user_id)
# #             if user.check_password(password) is True:
# #                 return user
# #         except User.DoesNotExist:
# #              pass
#
#     """
#     This is a ModelBacked that allows authentication with either a username or an email address.
#
#     """
# # def insertChecker(username):
# #         if '@' in username:
# #             insert = {'email': username}
# #         else:
# #             insert = {'mobile': username}
# #             if ((len(username)==11) and username.isdigit()):
# #                 return True
# #             else:
# #                 return False
#     #          try:
#     #           user = get_user_model().objects.get(**kwargs)
#     #           if user.check_password(password):
#     #             return user
#     #     except User.DoesNotExist:
#     #         return None
#     #
#     #
#     # def get_user(self, username):
#     #     try:
#     #         return get_user_model().objects.get(pk=username)
#     #     except get_user_model().DoesNotExist:
#     #         return None