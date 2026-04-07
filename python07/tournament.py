import ex0
import ex1
import ex2


def tournament(opponents: list[tuple[ex0.CreatureFactory,
                                     ex2.BattleStrategy]]) -> None:

    disply_opponents = []
    participants = []
    for fact, strat in opponents:
        creature: ex0.Creature = fact.create_base()
        strat_name: str = strat.__class__.__name__.replace("Strategy", "")
        disply_opponents.append(f"({creature.name}+{strat_name})")
        participants.append((creature, strat))

    print(f"[ {', '.join(disply_opponents)} ]")
    print("*** Tournament ***")
    print(f"{len(participants)} opponents involved\n")
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            c1, s1 = participants[i]
            c2, s2 = participants[j]
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                print(s1.act(c1))
                print(s2.act(c2))
                print()
            except ex2.InvalidStrategyException as e:
                print(e)


def main() -> None:
    t0 = [
        (ex0.FlameFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy())
    ]
    t1 = [
        (ex0.FlameFactory(), ex2.AggressiveStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy()),
    ]
    t2 = [
        (ex0.AquaFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy()),
        (ex1.TransformCreatureFactory(), ex2.AggressiveStrategy())
    ]
    print("Tournament 0 (basic)")
    tournament(t0)
    print("Tournament 1 (error)")
    tournament(t1)
    print("Tournament 2 (multiple)")
    tournament(t2)


if __name__ == "__main__":
    main()
