from socket import timeout
import sys
import random
import requests
from tbnu.Handler import Handler
from tbnu.Database import Database

__version__ = "1.0.1"


def check_latest_version(package="tbnu"):
    """Check if tbnu is at the latest version and let the user know if not"""
    # Try to query the pypi api. If the user isn't connected to the internet, abort the function
    try:
        response = requests.get(f"https://pypi.org/pypi/{package}/json", timeout=1)
    except requests.exceptions.ConnectionError:
        print("> Failed checking for updates < ")
        return

    latest_version = response.json()["info"]["version"]
    if latest_version != __version__:
        print(
            f"""
There is a new version of TBNU available!
You are at version {__version__}.
Upgrade to version {latest_version} using 'pip install --upgrade tbnu'
    """
        )


def main():
    # Only check if at latest version every 2 times
    # if the data dir exists and the db has already been created, load it
    if Database.PATH.exists():
        database = Database.load()
    else:
        database = Database()


    if random.randint(1, 2) == 2:
        check_latest_version()
    handler = Handler(sys.argv, database)
    # If the database is new, print the help message
    if database.new:
        handler.help()

    while True:
        try:
            inp = input(">> ")
            handler.parse_inp(inp)
        except KeyboardInterrupt:
            print("\nType 'exit' to exit the program")


if __name__ == "__main__":
    main()
