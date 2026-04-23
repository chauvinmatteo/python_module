import random

ACHIEVEMENTS_LIST: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Speed Runner", "Survivor", "Treasure Hunter",
    "Guild Master", "Sharp Mind", "First Steps", "Hidden Path Finder",
    "Unstoppable", "No Death"
]


def gen_player_achievements() -> set[str]:
    nb: int = random.randint(5, 10)
    selection: list[str] = random.sample(ACHIEVEMENTS_LIST, k=nb)
    return set(selection)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    MASTER_SET: set[str] = set(ACHIEVEMENTS_LIST)
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    common: set[str] = alice.intersection(bob, charlie, dylan)

    print(f"All distinct achievements: {all_distinct}\n")
    print(f"Common achievements: {common}")
    print()

    print(f"Only Alice has: {alice.difference(bob.union(charlie, dylan))}")
    print(f"Only Bob has: {bob.difference(alice.union(charlie, dylan))}")
    print(f"Only Charlie has: {charlie.difference(alice.union(bob, dylan))}")
    print(f"Only Dylan has: {dylan.difference(alice.union(bob, charlie))}")
    print()

    print(f"Alice is missing: {MASTER_SET.difference(alice)}")
    print(f"Bob is missing: {MASTER_SET.difference(bob)}")
    print(f"Charlie is missing: {MASTER_SET.difference(charlie)}")
    print(f"Dylan is missing: {MASTER_SET.difference(dylan)}")


if __name__ == "__main__":
    main()
