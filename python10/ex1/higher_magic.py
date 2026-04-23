from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restore {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if not callable(spell1) or not callable(spell2):
        raise TypeError("Spells need to be a function!")

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        first = spell1(target, power)
        second = spell2(target, power)
        combined = (first, second)
        return combined

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    if not callable(base_spell):
        raise TypeError("Base spell needs to be a function!")

    def amplified_spell(target, power):
        amplified = base_spell(target, power * multiplier)
        return amplified

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    if not callable(condition) or not callable(spell):
        raise TypeError("Condition and spell need to be functions!")

    def cond_cast(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return cond_cast


def spell_sequence(spells: list[Callable]):

    if not all(callable(s) for s in spells):
        raise TypeError("Spell needs to be a function!")

    def sequence(target, power):
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result

    return sequence


def main() -> None:

    print("\nTesting spell combiner...")
    try:
        combined_action = spell_combiner(fireball, heal)
        res_spell1, res_spell2 = combined_action("Dragon", 25)
        print(f"Combined spell result: {res_spell1}, {res_spell2}\n")
    except TypeError as e:
        print(f"Error: {e}\n")

    print("Testing power amplifier...")
    try:
        p = 10
        m = 3
        amplified_spell = power_amplifier(fireball, m)
        res_amplified = amplified_spell("Dragon", p)
        print(res_amplified)
        print(f"Original: {p}, Amplified: {p*m}\n")
    except TypeError as e:
        print(f"Error: {e}\n")

    print("Testing conditional casting...")
    try:
        def check_power(target, power):
            return power > 20
        casting = conditional_caster(check_power, fireball)
        valid_res = casting("Dragon", 22)
        print("Conditionial casting:" + valid_res)
    except TypeError as e:
        print(f"Error: {e}\n")

    print("\nTesting spell sequences...")
    try:
        sequence = spell_sequence([fireball, heal, fireball])
        print(f"Spell sequence: {sequence('Dragon', 20)}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
