import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base: ex0.Creature = factory.create_base()
    evolved: ex0.Creature = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(fact1: ex0.CreatureFactory, fact2: ex0.CreatureFactory) -> None:
    print("Testing battle")
    first_creature: ex0.Creature = fact1.create_base()
    second_creature: ex0.Creature = fact2.create_base()

    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
