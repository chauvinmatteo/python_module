import os
import sys
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...\n")
    mode: str | None = os.getenv("MATRIX_MODE")
    database: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str | None = os.getenv("LOG_LEVEL")
    zion_end: str | None = os.getenv("ZION_ENDPOINT")

    if None in [mode, database, api_key, log_level, zion_end]:
        print("CRITICAL ERROR: incomplete oracle generation.")
        print("Check if .env file has every variable")
        sys.exit(1)

    print("Configuration loaded:")
    print("Mode: " + mode)
    print("Database: " + ("Connected to local instance" if database
                          else "Not connected"))
    print("API Acces: " + ("Authenticated" if api_key
                           else "Missing or Invalid"))
    print("Log Level: " + log_level)
    print("Zion Network: " + ("Online" if zion_end
                              else "Offline"))


if __name__ == "__main__":
    main()
