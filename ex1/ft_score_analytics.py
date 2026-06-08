#!/usr/bin/env python3

import sys


def main() -> None:
    args = sys.argv
    print("=== Player Score Analytics ===")
    num_argv: int = len(args)
    if num_argv == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...\n"
        )
        return
    high_score: float = 0
    low_score: float = 0
    total_players: float = 0
    total_score: float = 0
    score_list: list[int] = []
    for score in args[1:]:
        try:
            score_int = int(score)
            total_players += 1
            total_score += score_int
            if high_score < score_int:
                high_score = score_int
            if score_int != 0 and low_score == 0:
                low_score = score_int
            elif low_score > score_int:
                low_score = score_int
            score_list.append(score_int)
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if not num_argv - 1 == len(score_list):
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...\n"
        )
        return
    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score/total_players}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}\n")


if __name__ == "__main__":
    main()
