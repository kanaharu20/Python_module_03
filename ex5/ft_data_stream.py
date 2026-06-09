#!/usr/bin/env python3

import random
import typing


def gen_event() -> tuple[str, str]:
    name_list: list[str] = ["alice", "bob", "charlie", "dylan"]
    action_list: list[str] = ["run", "eat", "sleep", "grab", "move", "swim"]
    name = random.choice(name_list)
    action = random.choice(action_list)
    return name, action


def consume_event(
        tuple_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while tuple_list:
        yield tuple_list.pop(random.randint(0, len(tuple_list) - 1))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for i in range(0, 1000):
        event = gen_event()
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    tuple_list: list[tuple[str, str]] = []

    for i in range(0, 10):
        tuple_list.append(gen_event())
    print(f"Built list of 10 events: {tuple_list}")

    for event in consume_event(tuple_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {tuple_list}")


if __name__ == "__main__":
    main()
