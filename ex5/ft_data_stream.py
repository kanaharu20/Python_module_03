#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    name_list: list[str] = ["alice", "bob", "charlie", "dylan"]
    action_list: list[str] = ["run", "eat", "sleep", "grab", "move", "swim"]
    while True:
        name = random.choice(name_list)
        action = random.choice(action_list)
        yield name, action


def consume_event(
        tuple_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while tuple_list:
        index: int = random.randint(0, len(tuple_list) - 1)
        yield tuple_list.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    tuple_list: list[tuple[str, str]] = []

    gen = gen_event()
    for i in range(10):
        tuple_list.append(next(gen))
    print(f"Built list of 10 events: {tuple_list}")

    consume = consume_event(tuple_list)
    for event_to_be_consumed in consume:
        print(f"Got event from list: {event_to_be_consumed}")
        print(f"Remains in list: {tuple_list}")


if __name__ == "__main__":
    main()
