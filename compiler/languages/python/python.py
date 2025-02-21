import subprocess
from compiler.languages.executor import Executor
from compiler.languages.python.analyzer import PythonAnalyzer
from compiler.languages.types import (
    ExecutorResult,
    ExecutorResultMetaData,
    AnalyzerResult,
)
import time


class PythonExecutor(Executor):
    def execute(self, code: str) -> ExecutorResult:
        analyzer_result: AnalyzerResult = PythonAnalyzer().analyze(code)
        if analyzer_result.result is not None:
            meta_data = ExecutorResultMetaData(
                execution_time=0.0, output_result=analyzer_result.result
            )
            return ExecutorResult(False, meta_data)
        start_time = time.time()
        try:
            execution_result = subprocess.run(
                ["python3", "-c", code], capture_output=True, text=True, timeout=7
            )
        except subprocess.TimeoutExpired:
            executor_result_meta_data = ExecutorResultMetaData(
                execution_time=7.0, output_result="Your code executing too long."
            )
            return ExecutorResult(
                execution_status=False, meta_data=executor_result_meta_data
            )
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        if execution_result.stderr:
            meta_data = ExecutorResultMetaData(
                execution_time=execution_time, output_result=execution_result.stderr
            )
            return ExecutorResult(False, meta_data)
        meta_data = ExecutorResultMetaData(
            execution_time=execution_time, output_result=execution_result.stdout
        )
        meta_data.output_result = execution_result.stdout
        return ExecutorResult(True, meta_data)
