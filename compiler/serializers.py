from rest_framework import serializers


class ExecutorResultMetaDataSerializer(serializers.Serializer):
    execution_time = serializers.CharField()
    output_result = serializers.CharField()


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5000)


class ExecutorResultSerializer(serializers.Serializer):
    execution_status = serializers.BooleanField()
    meta_data = ExecutorResultMetaDataSerializer()
