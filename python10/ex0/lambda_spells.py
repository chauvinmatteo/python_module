
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    l_sort = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return l_sort


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    l_filter = filter(lambda x: x['power'] >= min_power, mages)
    return list(l_filter)


def spell_transformer(spells: list[str]) -> list[str]:
    l_transform = map(lambda x: f"*{x}*", spells)
    return list(l_transform)


def mage_stats(mages: list[dict]) -> dict:
    max_pow = max(mages, key=lambda x: x['power'])
    min_pow = min(mages, key=lambda x: x['power'])
    mages_power = list(map(lambda m: m['power'], mages))
    average_pow: float = sum(mages_power) / len(mages_power)
    return {
        'max_power': max_pow['power'],
        'min_power': min_pow['power'],
        'avg_power': round(average_pow, 2)
    }


def main() -> None:

    print("Testing artifact sorter...")
    artifact: list[dict[str, str | int]] = [
        {
            'name': 'Staff',
            'power': 92,
            'type': 'Fire'
        },
        {
            'name': 'Orb',
            'power': 85,
            'type': 'Crystal'
        },
        {
            'name': 'Sword',
            'power': 70,
            'type': 'Dark'
        }
    ]
    sorted = artifact_sorter(artifact)
    print(f"{sorted[0]['type']} {sorted[0]['name']} ({sorted[0]['power']} "
          f"power) comes before {sorted[1]['type']} {sorted[1]['name']} "
          f"({sorted[1]['power']} power)\n")

    print("Testing power filter...")
    mages: list[dict[str, str | int]] = [
        {
            'name': 'Mage',
            'power': 38,
            'element': 'Fire'
        },
        {
            'name': 'Mage',
            'power': 47,
            'element': 'Water'
        },
        {
            'name': 'Mage',
            'power': 51,
            'element': 'Earth'
        }
    ]
    filtered = power_filter(mages, 40)
    for mage in filtered:
        print(f"{mage['element']} {mage['name']} has enough power "
              f"({mage['power']} power)")

    print("\nTesting spell transformer...")
    spells: list[str] = ['heal', 'fireball', 'shield']
    print(" ".join(spell_transformer(spells)) + "\n")

    print("Testing mage stats...")
    stats = mage_stats(artifact)
    print(f"The most powerful mage has {stats['max_power']} power")
    print(f"The least powerful mage has {stats['min_power']} power")
    print(f"The average power of mages is {stats['avg_power']} power")


if __name__ == "__main__":
    main()
