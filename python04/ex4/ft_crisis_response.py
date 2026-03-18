def main() -> None:
    test_file = None
    try:
        test_file = "lost_archive.txt"
        print(f"CRISIS ALERT: Attempting access to '{test_file}'...")
        with open(test_file, "r") as file:
            print("RESPONSE: Archive was found in storage matrix")
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()
    try:
        test_file = "classified_vault.txt"
        print(f"CRISIS ALERT: Attempting access to '{test_file}'...")
        with open(test_file, "r") as file:
            print("RESPONSE: Security protocols allow access")
            print(file.read())
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()
    try:
        test_file = "standard_archive.txt"
        print(f"ROUTINE ACCESS: Attempting access to '{test_file}'...")
        with open(test_file, "r") as file:
            print("SUCCESS: Archive recovered -"
                  "``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    main()
