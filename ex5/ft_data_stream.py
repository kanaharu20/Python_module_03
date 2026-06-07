#!/usr/bin/env python3

import typing, random

def gen_event() -> Generator[tuple, None, None]:
    name_list = ["alice", "bob", "charlie", "dylan"]
    action_list = ["run", "eat", "sleep", "grab", "move", "swim"]

    yield random.choice(name_list)
    yield random.choice(action_list)



def consume_event():


if __name__ == "__main__":
