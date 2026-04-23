from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counting() -> int:
        nonlocal count
        count += 1
        return count

    return counting


def spell_accumulator(initial_power: int) -> Callable:

    def accumulate(add_power) -> int:
        nonlocal initial_power
        initial_power += add_power
        return initial_power

    return accumulate


def enchantment_factory(enchantment_type) -> Callable:

    def enchantment(item_name: str) -> str:
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict:
    pass


def main() -> None:

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}\n")

    print("Testing spell accumulator...")
    base_power = 100
    accumulate = spell_accumulator(base_power)
    print(f"Base {base_power}, add 20: {accumulate(20)}")
    print(f"Base {base_power}, add 30: {accumulate(30)}\n")

    print("Testing enchantment factory...")
    enchantment1 = "Flaming"
    enchantment2 = "Frozen"
    enchanted_item1 = enchantment_factory(enchantment1)
    enchanted_item2 = enchantment_factory(enchantment2)
    print(enchanted_item1("Sword"))
    print(enchanted_item2("Shield"))

    print("Testing memory vault...")


if __name__ == "__main__":
    main()
