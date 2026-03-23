import random


def list_comprehension(player_list: list[str]) -> list[str]:
    put_capitalize: list[str] = [name.capitalize() for name in player_list]
    print(f"New list with all names capitalized: {put_capitalize}")
    only_capitalize: list[str] = [name for name in player_list
                                  if name.istitle()]
    print(f"New list of capitalized names only {only_capitalize}")
    return put_capitalize


def dict_comprehension(player_list: list[str]) -> None:
    players_score: dict[str, int] = {name: random.randint(0, 1000)
                                     for name in player_list}
    print(f"Score dict: {players_score}")
    total_score: int = sum(players_score.values())
    average_score: float = total_score / len(players_score)
    print(f"Score average is {average_score:.2f}")
    high_score: dict[str, int] = {name: score
                                  for name, score in players_score.items()
                                  if score > average_score}
    print(f"High scores: {high_score}")


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")
    clean_list: list[str] = list_comprehension(players)
    print()
    dict_comprehension(clean_list)


if __name__ == "__main__":
    main()
