from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User




class emailBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
             pass