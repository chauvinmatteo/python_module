import ex0


def firetype_factory() -> None:
    print("Testing factory")
    flame_factory = ex0.FlameFactory()
    flameling = flame_factory.create_base()
    pyrodon = flame_factory.create_evolved()
    print(flameling.describe())
    print(pyrodon.describe())


if __name__ == "__main__":
    main()
