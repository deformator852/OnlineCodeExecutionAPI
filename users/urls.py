from django.urls import path
from users.views import GiveCode, SaveCode, UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", UserRegistrationView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("code/save/", SaveCode.as_view()),
    path("code/<int:code_id>/", GiveCode.as_view()),
]
