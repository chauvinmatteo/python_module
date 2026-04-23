from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "alice", "bob", "charlie", "dylan"
    ]
    event: list[str] = [
        "swim", "run", "eat", "sleep", "move", "climb"
    ]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(event)
        yield (name, action)


def consume_event(
        event_list: list[tuple[str, str]]) -> Generator[
            tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randrange(len(event_list))
        remove_event = event_list.pop(index)
        yield remove_event


def main() -> None:
    stream: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
    ten_event: list[tuple[str, str]] = []
    for i in range(10):
        name, action = next(stream)
        ten_event.append((name, action))
    print(f"Built list of 10 event: {ten_event}")
    for event in consume_event(ten_event):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_event}")


if __name__ == "__main__":
    main()
