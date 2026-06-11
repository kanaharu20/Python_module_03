#!/usr/bin/env python3

import sys


def main() -> None:
    args = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    num_argv: int = len(args)
    if num_argv < 2:
        print(
            "No arguments provided!\n"
            "Total arguments: 1"
        )
    else:
        print(f"Arguments received: {num_argv - 1}")
        j: int = 1
        for i in args[1:]:
            print(
                f"Argument {j}: {i}"
            )
            j += 1
        print(f"Total arguments: {num_argv}")


if __name__ == "__main__":
    main()
