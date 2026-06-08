#!/usr/bin/env python3

import math


def get_player_pos() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    while True:
        try:
            raw1: str = input(
                "Enter new coordinates as "
                "floats in format 'x,y,z': "
            )
            if not 3 == len(raw1.split(",")):
                raise SyntaxError("Invalid syntax")
            x1, y1, z1 = (float(p) for p in raw1.split(","))
            point_player1: tuple[float, float, float] = (x1, y1, z1)
            break
        except (SyntaxError, ValueError) as e:
            print(e)
    print(f"Got a first tuple: {point_player1}")
    print(
        f"It includes: X={point_player1[0]}, "
        f"Y={point_player1[1]}, Z={point_player1[2]}"
    )
    distance_center = math.sqrt(
        point_player1[0]**2 + point_player1[1]**2 + point_player1[2]**2
    )
    print(f"Distance to center: {round(distance_center, 4)}\n")

    print("Get a second aet of coordinates")
    while True:
        try:
            raw2: str = input(
                "Enter new coordinates "
                "as floats in format 'x,y,z': "
            )
            if not 3 == len(raw2.split(",")):
                raise SyntaxError("Invalid syntax")
            x2, y2, z2 = (float(p) for p in raw2.split(","))
            point_player2: tuple[float, float, float] = (x2, y2, z2)
            break
        except (SyntaxError, ValueError) as e:
            print(e)
    distance_inbetween = math.sqrt(
        (point_player1[0] - point_player2[0])**2
        + (point_player1[1] - point_player2[1])**2
        + (point_player1[2] - point_player2[2])**2)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(distance_inbetween, 4)}"
        )


if __name__ == "__main__":
    get_player_pos()
