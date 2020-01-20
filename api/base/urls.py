from django.contrib import admin
from django.urls import path, include

from api.base.views.authTokenView import AuthTokenView
from api.base.views.userView import UserView

urlpatterns = [
    path('auth/register/', UserView.as_view()),
    # path('profile/', UserView.as_view()),
    path('auth/profile/<uuid:guid>[0-99]/', UserView.as_view()), # TODO : regex for uid pass
    path('auth/login/',AuthTokenView.as_view()),
    path('auth/login/social', include('rest_auth.urls')),
    # path('users/<int:pk>/', UserView.as_view()),
    ]
