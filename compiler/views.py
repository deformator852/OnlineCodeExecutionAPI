from rest_framework.views import APIView
from rest_framework.response import Response
from compiler.languages.python.python import PythonExecutor
from compiler.languages.types import ExecutorResult
from compiler.serializers import CodeSerializer, ExecutorResultSerializer


class PythonCodeAPI(APIView):
    def post(self, request):
        code_serializer = CodeSerializer(data=request.data)
        if code_serializer.is_valid():
            code = code_serializer.validated_data.get("code", "")  # type: ignore
            execution_result: ExecutorResult = PythonExecutor().execute(code)
            execution_result_serializer = ExecutorResultSerializer(execution_result)
            return Response(execution_result_serializer.data)
        return Response(code_serializer.errors, status=400)
