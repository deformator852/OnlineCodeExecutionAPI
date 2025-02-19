from compiler.languages.analyzer import Analyzer
import ast

from compiler.languages.types import AnalyzerResult

forbidden_modules = [
    "os",
    "shutil",
    "pathlib",
    "aiohttp",
    "requests",
    "urllib",
    "pathlib",
    "glob",
    "tempfile",
    "subprocess"

]


class PythonAnalyzer(Analyzer):
    def analyze(self, code: str) -> AnalyzerResult:
        result = {}
        code_ast = ast.parse(code)
        for node in ast.walk(code_ast):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                forbidden_imports: list = self.__imports_analyze(node)
                if forbidden_imports:
                    result["forbidden_modules"] = forbidden_imports
        if result:
            return AnalyzerResult(status=False, result=result)
        return AnalyzerResult(status=True, result=None)

    def __imports_analyze(self, node: ast.Import | ast.ImportFrom) -> list:
        result = []
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in forbidden_modules:
                    result.append({"module": alias.name, "line": node.lineno, "column": node.col_offset})
                    return result
            return []
        if node.module in forbidden_modules:
            result.append({"module": node.module, "line": node.lineno, "column": node.col_offset})
        return result
