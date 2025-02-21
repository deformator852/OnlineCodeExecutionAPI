from dataclasses import dataclass


@dataclass
class AnalyzerResult:
    result: dict[str, list] | None = None


@dataclass
class ExecutorResultMetaData:
    execution_time: float
    output_result: dict | str


@dataclass
class ExecutorResult:
    execution_status: bool
    meta_data: ExecutorResultMetaData
