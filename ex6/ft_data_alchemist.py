#!/usr/bin/env python3

import random


def main():
    print("=== Game Data Alchemist ===\n")

    initial_name_list: list = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
        ]
    print(f"Initial list of players: {initial_name_list}")
    all_capitalized_name_list: list = []
    for name in initial_name_list:
        all_capitalized_name_list.append(name.capitalize())
    print(f"New list with all names capitalized: {all_capitalized_name_list}")
    only_capitalized_name_list: list = []
    for name in initial_name_list:
        if name == name.capitalize():
            only_capitalized_name_list.append(name)
    print(f"New list of capitalized names only: {only_capitalized_name_list}")

    score_dict: dict = {
        name: random.randint(0, 1000) for name in initial_name_list
        }
    print(f"Score dict: {score_dict}")

    total_score: float = sum(score_dict.values())

    score_average: float = total_score/len(score_dict)

    print(f"Score average is {round(score_average, 2)}")

    high_scored_name_dict: dict = {}
    for content in score_dict:
        if score_dict[content] > score_average:
            high_scored_name_dict.update({content: score_dict[content]})
    print(f"High scores: {high_scored_name_dict}")


if __name__ == "__main__":
    main()
