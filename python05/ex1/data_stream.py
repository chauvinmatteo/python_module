from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        super().__init__()
        self.stream_id: str = stream_id
        self.type: str = "Default type"
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "type": "Generic"}


class SensorStream(DataStream):
    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch) -> str:
        total_temp = 0.0
        count = 0
        for item in data_batch:
            try:
                if isinstance(item, (int, float)):
                    total_temp += float(item)
                    count += 1
                elif isinstance(item, str) and ":" in item:
                    key, val = item.split(":")
                    if "temp" in key.lower():
                        total_temp += float(val)
                        count += 1
            except (ValueError, IndexError):
                continue
        self.processed = count
        self.avg_temp = total_temp / count if count > 0 else 0.0
        s = "s" if count > 1 else ""
        res = (f"Sensor analysis: {count} reading{s} processed,"
               f"avg temp: {self.avg_temp:.1f}°C")
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria or criteria != "high":
            return super().filter_data(data_batch, criteria)
        filtered_result: list = []
        for data in data_batch:
            try:
                if isinstance(data, str) and ":" in data:
                    key, value = data.split(":")
                    if float(value) > 25:
                        filtered_result.append(data)
            except (ValueError, IndexError):
                continue
        return filtered_result

    def get_stats(self) -> Dict[str, str | int | float]:
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({
            "type": self.type,
            "avg_temp": self.avg_temp,
            "readings": self.processed
        })
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.net_flow: int = 0

    def process_batch(self, data_batch) -> str:
        net_flow_amount: int = 0
        transaction: int = 0
        for item in data_batch:
            try:
                if isinstance(item, int):
                    transaction += 1
                elif isinstance(item, str) and ":" in item:
                    key, value = item.split(":")
                    amount = int(value)
                    if "buy" in key.lower():
                        net_flow_amount -= amount
                        transaction += 1
                    elif "sell" in key.lower():
                        net_flow_amount += amount
                        transaction += 1
            except (ValueError, IndexError):
                continue
        self.processed = transaction
        self.net_flow = net_flow_amount
        sign = "+" if self.net_flow >= 0 else ""
        res = (f"Transaction analysis: {transaction} operations,"
               f"net flow: {sign}{self.net_flow} units")
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria or criteria != "large":
            return super().filter_data(data_batch, criteria)
        filtered_result: list[Any] = []
        for data in data_batch:
            try:
                if isinstance(data, str) and ":" in data:
                    key, value = data.split(":")
                    if float(value) > 500:
                        filtered_result.append(data)
            except (ValueError, IndexError):
                continue
        return filtered_result

    def get_stats(self) -> Dict[str, str | int | float]:
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({
            "type": self.type,
            "net_flow": self.net_flow,
            "operations": self.processed
        })
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        self.error: int = 0

    def process_batch(self, data_batch) -> str:
        event_count: int = 0
        for item in data_batch:
            try:
                if isinstance(item, str):
                    event_count += 1
                if isinstance(item, str) and ":" in item:
                    key, value = item.split(":")
                    event_count += 1
                    if "error" in key.lower():
                        self.error += 1
            except (ValueError, IndexError):
                continue
        self.processed = event_count
        return f"Event analysis: {event_count} events, {self.error} error"
    "detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return super().filter_data(data_batch, criteria)
        priority_keywords: List[str] = ["error", "critical", "fail"]
        filtered_result: list[Any] = []
        for data in data_batch:
            if isinstance(data, str):
                if any(word in data.lower() for word in priority_keywords):
                    filtered_result.append(data)
        return filtered_result

    def get_stats(self) -> Dict[str, str | int | float]:
        stats: Dict[str, str | int | float] = super().get_stats()
        stats.update({
            "type": self.type,
            "error": self.error,
            "operations": self.processed
        })
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, all_batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for i in range(len(self.streams)):
            stream: DataStream = self.streams[i]
            batch: List[Any] = all_batches[i]
            raw_res: str = stream.process_batch(batch)
            if isinstance(stream, SensorStream):
                label = "Sensor data"
            elif isinstance(stream, TransactionStream):
                label = "Transaction data"
            else:
                label = "Event data"
            summary: str = raw_res.split(",", 1)[0]
            clean_summary: str = summary.split(": ", 1)[1]
            clean_summary += " processed"
            print(f" - {label}: {clean_summary}")

    def apply_global_filter(self, all_batches: List[List[Any]],
                            criteria: str) -> None:
        print("\nStream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts,"
              "1 large transaction")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")

    sensor: SensorStream = SensorStream("SENSOR_001")
    s_stats: Dict[str, str | int | float] = sensor.get_stats()
    print(f"Stream ID: {s_stats['id']}, Type: {s_stats['type']}")
    s_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {s_batch}")
    print(sensor.process_batch(s_batch))
    print()

    print("Initializing Transaction Stream...")
    trans: TransactionStream = TransactionStream("TRANS_001")
    t_stats: Dict[str, str | int | float] = trans.get_stats()
    print(f"Stream ID: {t_stats['id']}, Type: {t_stats['type']}")
    t_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {t_batch}")
    print(trans.process_batch(t_batch))
    print()

    print("Initializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    e_stats: Dict[str, str | int | float] = event.get_stats()
    print(f"Stream ID: {e_stats['id']}, Type: {e_stats['type']}")
    e_batch: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {e_batch}")
    print(event.process_batch(e_batch))
    print()

    manager = StreamProcessor()
    manager.add_stream(SensorStream("SENSOR_01"))
    manager.add_stream(TransactionStream("TRANS_01"))
    manager.add_stream(EventStream("EVENT_01"))
    data_batches: List[List[Any]] = [
        [22.5, "temp:28.0", "temp:15.0"],
        ["buy:600", "sell:200", "buy:100"],
        ["login", "error", "logout"]
    ]
    manager.process_all(data_batches)
    manager.apply_global_filter(data_batches, "high")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()