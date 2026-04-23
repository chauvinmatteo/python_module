def main() -> None:
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    try:
        with open("classified_data.txt", "r") as file:
            print("SECURE EXTRACTION:")
            print(file.read())
            print()
        with open("standard_archive.txt", "w") as file:
            print("SECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    except FileNotFoundError:
        print("The file doesnt exist")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    main()
