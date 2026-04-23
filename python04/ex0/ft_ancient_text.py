from io import TextIOWrapper


def main() -> None:
    text = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {text}")
    try:
        file: TextIOWrapper = open(text)
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(file.read())
        print()
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        if file is not None:
            file.close()
            print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    main()
