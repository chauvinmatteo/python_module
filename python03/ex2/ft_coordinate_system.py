import math


def get_player_pos() -> tuple[float, float, float]:
    prompt: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        position: str = input(prompt)
        parts: list[str] = position.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = []
            for pos in parts:
                clean_val: str = pos.strip()
                player_pos = float(clean_val)
                coords.append(player_pos)
            return (coords[0], coords[1], coords[2])
        except ValueError as e:
            print(f"Error on parameter '{clean_val}': {e}")


def calculate_distance(pos_1: tuple[float, float, float],
                       pos_2: tuple[float, float, float]) -> float:
    x1: float
    y1: float
    z1: float
    x1, y1, z1 = pos_1
    x2: float
    y2: float
    z2: float
    x2,  y2, z2 = pos_2
    res: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return res


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance: float = calculate_distance(pos1, (0, 0, 0))
    print(f"Distance to center: {distance:.4f}\n")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    distance2: float = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {distance2:.4f}")


if __name__ == "__main__":
    main()
