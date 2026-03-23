import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    nums_args: int = len(sys.argv) - 1
    if nums_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {nums_args}")
        for i in range(1, len(sys.argv)):
            print(f"Arguments {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
