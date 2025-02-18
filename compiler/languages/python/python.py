import subprocess
from compiler.languages.executor import Executor
from compiler.languages.types import ExecutorResult, ExecutorResultMetaData
import time


class PythonExecutor(Executor):
    def execute(self, code: str) -> ExecutorResult:
        start_time = time.time()
        execution_result = subprocess.run(["python3", "-c", code], capture_output=True, text=True)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        if execution_result.stdout:
            meta_data = ExecutorResultMetaData(execution_time=execution_time, output_result=execution_result.stdout)
            meta_data.output_result = execution_result.stdout
            return ExecutorResult(True, meta_data)
        meta_data = ExecutorResultMetaData(execution_time=execution_time, output_result=execution_result.stderr)
        return ExecutorResult(False, meta_data)
