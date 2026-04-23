
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    l_sort = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    #print(l_sort)
    return l_sort


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    l_filter = filter(lambda x: x['power'] >= min_power, mages)
    #print(list(l_filter))
    return list(l_filter)


def spell_transformer(spells: list[str]) -> list[str]:
    l_transform = map(lambda x: f"*{x}*", spells)
    #print(list(l_transform))
    return list(l_transform)


def mage_stats(mages: list[dict]) -> dict:
    max_pow = max(mages, key=lambda x: x['power'])
   # print(max_pow)
    min_pow = min(mages, key=lambda x: x['power'])
   # print(min_pow)
    mages_power = list(map(lambda m: m['power'], mages))
    average_pow: float = sum(mages_power) / len(mages_power)
   # print(round(average_pow, 2))
    return {
        'max_power': max_pow,
        'min_power': min_pow,
        'avg_power': average_pow
    }


def main() -> None:
    artifact: list[dict[str, str | int]] = [
        {
            'name': 'Staff',
            'power': 92,
            'element': 'Fire'
        },
        {
            'name': 'Orb',
            'power': 85,
            'element': 'Crystal'
        },
        {
            'name': 'Sword',
            'power': 88,
            'element': 'Dark'
        }
    ]
    spells: list[str] = ['heal', 'fireball', 'shield']
    print("Testing artifact sorter...")
    sorted = artifact_sorter(artifact)
    print(f"{sorted[0]['element']} {sorted[0]['name']}")

    power_filter(artifact, 3)
    spell_transformer(spells)
    mage_stats(artifact)


if __name__ == "__main__":
    main()
