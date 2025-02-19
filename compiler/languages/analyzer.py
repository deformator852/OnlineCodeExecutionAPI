from abc import ABC, abstractmethod
from compiler.languages.types import AnalyzerResult


class Analyzer(ABC):
    @abstractmethod
    def analyze(self, code: str) -> AnalyzerResult: ...
