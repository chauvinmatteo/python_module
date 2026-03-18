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

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ":" in data:
            print("Validation: Log entry verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        if "Error:" in result:
            return f"Output: {result}"
        prefix = "[ALERT]" if "ERROR" in result else "[INFO]"
        return f"Output: {prefix} {result}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")
    np = NumericProcessor()
    val_n: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {val_n}")
    print(f"Output: {np.process(val_n)}")
    print()
    print("Initializing Text Processor...")
    tp = TextProcessor()
    val_t = "Hello Nexus World"
    print(f"Processing data: \"{val_t}\"")
    print(f"Output: {tp.process(val_t)}")
    print()
    print("Initializing Log Processor...")
    lp = LogProcessor()
    val_l = "ERROR: Connection timeout"
    print(f"Processing data: \"{val_l}\"")
    print(f"Output: {lp.format_output(lp.process(val_l))}")
    print()
    print("=== Polymorphic Processing Demo ===")
    print()
    print("Processing multiple data types through same interface...")
    procs: list[NumericProcessor | TextProcessor |
                LogProcessor] = [NumericProcessor(), TextProcessor(),
                                 LogProcessor()]
    datas: list[list[int] | str] = [[1, 2, 3], "Data streams",
                                    "INFO: System ready"]
    for i in range(len(procs)):
        proc: NumericProcessor | TextProcessor | LogProcessor = procs[i]
        data: list[int] | str = datas[i]
        raw_result: str = proc.process(data)
        final_string: str = proc.format_output(raw_result)
        clean_result: str = final_string.replace("Output: ", "")
        print(f"Result {i + 1}: {clean_result}")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
