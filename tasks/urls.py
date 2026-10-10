from django.urls import path
from .views import users, user_detail, create_user

urlpatterns=[
    path("users/", users),
    path("users/<int:user_id>/", user_detail),
    path("users/create", create_user)
]