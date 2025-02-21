from django.urls import path
from compiler.views import PythonCodeAPI

urlpatterns = [
    path("code/python", PythonCodeAPI.as_view()),
]
