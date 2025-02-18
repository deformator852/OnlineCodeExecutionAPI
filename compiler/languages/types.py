from dataclasses import dataclass


@dataclass
class ExecutorResultMetaData:
    execution_time: str
    output_result: str


@dataclass
class ExecutorResult:
    execution_status: bool
    meta_data: ExecutorResultMetaData


@dataclass
class AnalyzerResult: ...
