from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Code
from users.serializers import CodeSerializer, UserRegistrationSerializer
from rest_framework.permissions import AllowAny


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "created"})
        return Response(serializer.errors, status=400)


class SaveCode(APIView):
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data.get("code")  # type:ignore
            Code.objects.create(user=request.user, code=code).save()
            return Response({"msg": "saved"})


class GiveCode(APIView):
    def get(self, request, code_id: int):
        code = Code.objects.get(pk=code_id, user=request.user)
        if code:
            serializer = CodeSerializer(code)
            return Response({"code": serializer.data})
        return Response({"msg": "Code not found"}, status=404)
