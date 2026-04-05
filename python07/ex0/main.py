from ex0.CreatureCard import CreatureCard


def main() -> None:
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 1, "Common", 2, 3)
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    game_state: dict = {}
    game_state = dragon.play(game_state)
    mana_available = 6
    print(f"Playing {dragon.name} with {mana_available} mana available")
    if dragon.is_playable(mana_available):
        print("Playable: True")
        print(f"Play Result: {game_state}")
    else:
        print("Playable: False")
    print()

    print(f"{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")
    print()

    print("Testing insufficient mana (3 available):")
    mana_available = 3
    if dragon.is_playable(mana_available) is False:
        print("Playable: False")


if __name__ == "__main__":
    main()
