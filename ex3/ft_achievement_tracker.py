#!/usr/bin/env python3

import random


def gen_player_achievements() -> None:
    print("=== Achievement Tracker System ===\n")
    all_achievements: set[str] = {
        'Crafting Genius', 'Strategist',
        'World Savior', 'Speed Runner', 'Survivor',
        'Master Explorer', 'Treasure Hunter',
        'Unstoppable', 'First Steps', 'Collector Supreme',
        'Untouchable', 'Sharp Mind', 'Boss Slayer'}

    num_achievement: int = random.randint(0, len(all_achievements))
    alice_achievements: set[str] = set(random.sample(
        list(all_achievements), num_achievement))

    num_achievement = random.randint(0, len(all_achievements))
    bob_achievements: set[str] = set(random.sample(
        list(all_achievements), num_achievement))

    num_achievement = random.randint(0, len(all_achievements))
    charlie_achievements: set[str] = set(random.sample(
        list(all_achievements), num_achievement))

    num_achievement = random.randint(0, len(all_achievements))
    dylan_achievements: set[str] = set(random.sample(
        list(all_achievements), num_achievement))

    print(f"Player Alice: {alice_achievements}")

    print(f"Player Bob: {bob_achievements}")

    print(f"Player Charlie: {charlie_achievements}")

    print(f"Player Dylan: {dylan_achievements}")

    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements: set[str] = alice_achievements.intersection(
        bob_achievements)
    common_achievements = common_achievements.intersection(
        charlie_achievements)
    common_achievements = common_achievements.intersection(dylan_achievements)

    print(f"\nCommon achievements: {common_achievements}")

    but_alice: set[str] = bob_achievements.union(charlie_achievements)
    but_alice = but_alice.union(dylan_achievements)
    only_alice: set[str] = alice_achievements.difference(but_alice)
    print(f"Only Alice has: {only_alice}")

    but_bob: set[str] = alice_achievements.union(
        charlie_achievements).union(dylan_achievements)
    only_bob = bob_achievements.difference(but_bob)
    print(f"Only Bob has: {only_bob}")

    but_charlie: set[str] = alice_achievements.union(
        bob_achievements).union(dylan_achievements)
    only_charlie = charlie_achievements.difference(but_charlie)
    print(f"Only Charlie has: {only_charlie}")

    but_dylan: set[str] = alice_achievements.union(
        bob_achievements).union(charlie_achievements)
    only_dylan = dylan_achievements.difference(but_dylan)
    print(f"Only Dylan has: {only_dylan}")

    print(
        "\nAlice is missing: "
        f"{all_achievements.difference(alice_achievements)}"
        )

    print(f"Bob is missing: {all_achievements.difference(bob_achievements)}")

    print(
        "Charlie is missing: "
        f"{all_achievements.difference(charlie_achievements)}"
    )

    print(
        f"Dylan is missing: {all_achievements.difference(dylan_achievements)}")


if __name__ == "__main__":
    gen_player_achievements()
