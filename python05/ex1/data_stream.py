from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[Any] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data to output")
        item = self._data.pop(0)
        current_rank: int = self._rank
        self._rank += 1
        return (current_rank, str(item))

    def queue_size(self) -> int:
        return len(self._data)

    def total_processed(self) -> int:
        return self.queue_size() + self._rank


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            return all(type(x) in (int, float) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self._data.extend(data)
        else:
            self._data.append(data)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._data.extend(data)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) and isinstance(value, str)
                       for key, value in data.items())
        if isinstance(data, list):
            return all(
                isinstance(d, dict) and all(isinstance(key, str)
                                            and isinstance(value, str)
                                            for key, value in d.items())
                for d in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, dict):
            data = [data]
        for item in data:
            str_representation: str = ": ".join(item.values())
            self._data.append(str_representation)


class DataStream:
    def __init__(self) -> None:
        self._registered_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._registered_processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            for proc in self._registered_processors:
                if proc.validate(data):
                    proc.ingest(data)
                    break
            else:
                print(f"DataStream error - "
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        if not self._registered_processors:
            print("No processor found, no data")
        else:
            for proc in self._registered_processors:
                raw_name: str = proc.__class__.__name__
                proc_name: str = raw_name.replace("Processor", " Processor")
                remaining: int = proc.queue_size()
                total: int = proc.total_processed()
                print(f"{proc_name}: total {total} items processed, "
                      f"remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())
    first_data: list[Any] = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'}, {
              'log_level': 'INFO',
         'log_message': 'User wil isconnected'}],
        42, ['Hi', 'five']
        ]
    print(f"\nSend first batch of data on stream: {first_data}")
    stream.process_stream(first_data)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(first_data)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    for proc in stream._registered_processors:
        if proc.__class__.__name__ == "NumericProcessor":
            for _ in range(3):
                proc.output()
        elif proc.__class__.__name__ == "TextProcessor":
            for _ in range(2):
                proc.output()
        elif proc.__class__.__name__ == "LogProcessor":
            for _ in range(1):
                proc.output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
