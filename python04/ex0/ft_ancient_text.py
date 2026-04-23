from io import TextIOWrapper


def main() -> None:
    text = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {text}")
    try:
        file: TextIOWrapper = open(text, "r")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(file.read())
        print()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if file is not None:
            file.close()
            print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    main()
