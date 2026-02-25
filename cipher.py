import sys
from encryption import encrypt, decrypt

USAGE = """
Usage:
  python cipher.py encrypt "message"
  python cipher.py decrypt "message"

Examples:
  python cipher.py encrypt "Dublin"
  python cipher.py decrypt "Evcmjo"
"""

def main():
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit(1)

    command = sys.argv[1].lower()
    message = sys.argv[2]

    try:
        if command == "encrypt":
            print(encrypt(message))
            print("### Message encrypted ###")
        elif command == "decrypt":
            print(decrypt(message))
            print("### Message decrypted ###")
        else:
            print("Unknown command")
            print(USAGE)
            sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}")
        sys.exit(2)

if __name__ == "__main__":
    main()
