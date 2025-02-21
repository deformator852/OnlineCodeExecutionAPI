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
    "subprocess",
]


class PythonAnalyzer(Analyzer):
    def analyze(self, code: str) -> AnalyzerResult:
        result = {"forbidden_modules": [], "infinity_loops": []}
        code_ast = ast.parse(code)
        for node in ast.walk(code_ast):
            if isinstance(node, (ast.While, ast.For)):
                infinity_loops = self.__infinity_loops(node)
                result["infinity_loops"].extend(infinity_loops)
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                forbidden_imports: list = self.__imports_analyze(node)
                if forbidden_imports:
                    result["forbidden_modules"].extend(forbidden_imports)
        if result:
            return AnalyzerResult(result=result)
        return AnalyzerResult(result=None)

    def __infinity_loops(self, node: ast.While | ast.For) -> list:
        result = []
        if isinstance(node, ast.While):
            condition = node.test
            if isinstance(condition, ast.Constant) and condition.value is True:
                result.append(
                    {"type": "while", "line": node.lineno, "column": node.col_offset}
                )
        else:
            if isinstance(node.iter, ast.Call):
                if isinstance(node.iter.func, ast.Name) and node.iter.func.id == "iter":
                    if len(node.iter.args) == 2:
                        result.append(
                            {
                                "type": "for",
                                "line": node.lineno,
                                "column": node.col_offset,
                            }
                        )
        return result

    def __imports_analyze(self, node: ast.Import | ast.ImportFrom) -> list:
        result = []
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in forbidden_modules:
                    result.append(
                        {
                            "module": alias.name,
                            "line": node.lineno,
                            "column": node.col_offset,
                        }
                    )
                    return result
            return []
        if node.module in forbidden_modules:
            result.append(
                {"module": node.module, "line": node.lineno, "column": node.col_offset}
            )
        return result
