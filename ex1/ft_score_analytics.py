#!/usr/bin/env python3

import sys

def main() -> None:
    args = sys.argv
    print("=== Player Score Analytics ===")
    num_argv = len(args)
    if num_argv == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return
    high_score = 0
    low_score = 0
    total_players = 0
    total_score = 0
    score_list = []
    for i in range(0, num_argv - 1):
        try:
            args_int = int(args[i])
            total_players += 1
            total_score += args_int
            if high_score < args_int:
                high_score = args_int
            if not args_int == 0 & low_score == 0:
                low_score = args_int
            elif low_score > args_int:
                low_score = args_int
            score_list.append()
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
