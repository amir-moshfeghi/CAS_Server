from datetime import  datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db import models



# class UserModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     nick_name = models.CharField(max_length=100)
#     password = models.TextField(blank=False)
#     email = models.EmailField(blank=False)
#     mobile = models.CharField(blank=True,max_length=100)
#     address = models.TextField(blank=True)
#     # photo = models.ImageField(blank=True)
#     type = models.TextField(blank=True)
#     # last_login_date = models.DateTimeField(blank=True,default=datetime.now())
#     # last_edit = models.DateTimeField(blank=True)
#
#
#     class Meta:
#         ordering = ['id']

class UserModel(AbstractUser):
        id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=100,unique=True)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        nick_name = models.CharField(max_length=100)
        password = models.TextField(blank=False)
        email = models.EmailField(blank=False)
        mobile = models.CharField(blank=True,max_length=100)
        address = models.TextField(blank=True)
        # photo = models.ImageField(blank=True)
        type = models.TextField(blank=True)
        # last_login_date = models.DateTimeField(blank=True,default=datetime.now())
        # last_edit = models.DateTimeField(blank=True)
        # USERNAME_FIELD = 'username'
        def __str__(self):
           return self.username
#
# class UserModel(BaseModel):
#     customer_id = models.CharField(max_length=10)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.TextField()
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
#
#     objects = CustomerManager()
#
#     def __str__(self):
#         return self.customer_id