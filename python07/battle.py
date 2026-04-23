import ex0


def test_factory(factory):
    print("Testing factory")
    base: Creature = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(fact1, fact2):
    print("Testing battle")
    c1 = fact1.create_base()
    c2 = fact2.create_base()

    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


def main():
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
