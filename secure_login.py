# Educational improved version
import getpass
import hashlib
import hmac
import os

MAX_ATTEMPTS = 3
USERNAME = "admin"

# Demo only. A real app should store password hashes securely in a database/credential store.
demo_password = os.environ.get("DEMO_PASSWORD", "ChangeMe_123!")
salt = os.urandom(16)
stored_hash = hashlib.pbkdf2_hmac("sha256", demo_password.encode(), salt, 200_000)

for attempt in range(MAX_ATTEMPTS):
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    entered_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)

    if username == USERNAME and hmac.compare_digest(entered_hash, stored_hash):
        print("Login successful")
        break

    remaining = MAX_ATTEMPTS - attempt - 1
    if remaining:
        print(f"Invalid username or password. Attempts left: {remaining}")
    else:
        print("Login failed. Try again later.")
