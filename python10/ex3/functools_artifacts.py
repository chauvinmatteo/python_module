from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }
    if not spells:
        return 0
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(ops[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} (Power: {power})"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="Fire")
    ice = partial(base_enchantment, power=50, element="Ice")
    earth = partial(base_enchantment, power=50, element="Earth")
    return {
        "fire": fire,
        "ice": ice,
        "earth": earth
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


def main() -> None:

    print("Testing spell reducer...")
    try:
        powers = [10, 20, 30, 40]
        print(f"Sum: {spell_reducer(powers, 'add')}")
        print(f"Product: {spell_reducer(powers, 'multiply')}")
        print(f"Max: {spell_reducer(powers, 'max')}")
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant['fire'](target='Troll'))
    print(enchant['ice'](target='Goblin'))
    print(enchant['earth'](target='Dragon'))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
