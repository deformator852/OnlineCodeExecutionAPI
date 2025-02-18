from abc import ABC, abstractmethod
from compiler.languages.types import ExecutorResult


class Executor(ABC):
    @abstractmethod
    def execute(self, code: str) -> ExecutorResult: ...
