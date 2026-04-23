from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"
        len_data: int = len(data)
        sum_data: int = sum(data)
        average_data: float = sum_data / len_data
        result: str = (f"Processed {len_data} numeric values"
                       f", sum={sum_data}, avg={average_data}")
        return result

    def validate(self, data: list[int]) -> bool:
        if not isinstance(data, list):
            return False
        if data and all(isinstance(x, (int, float)) for x in data):
            print("Validation: Numeric data verified")
            return True
        else:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: data is not a str"
        len_data: int = len(data)
        word_cnt: int = len(data.split())
        result: str = (f"Processed text: {len_data} characters,"
                       f"{word_cnt} words")
        return result

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            return False
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: invalid log format"
        parts: str = data.split(":", 1)
        level: str = parts[0]
        message: str = parts[1]
        return f"{level} level detected: {message}"

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            return False
        has_info: bool = "Error" in data or "INFO" in data
        has_sep: bool = ":" in data
        if has_info and has_sep:
            print("Validation: Log entry verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        prefix: str = "[ALERT]" if "ERROR" in result else "[INFO]"
        return f"Output: {prefix} {result}"


def polymorphism_process(data: Any, processor: list[DataProcessor]) -> None:
    for i in range(3):
        data_processor: DataProcessor = processor[i]
        try:
            print(f"Result {i + 1}: {data_processor.process(data[i])}")
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


def main():
    print("")
    data: [ [1, 2, 3,\