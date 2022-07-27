import sys, os, platform, random
from tbnu.Database import Database
from argparse import ArgumentParser
from tbnu.aesthetics.colors import Colors
from tbnu.aesthetics.logos import LOGOS


class Handler:
    def __init__(self, argv: sys.argv, database) -> None:
        self.argv = argv
        self.database = database
        # Tracks if any cli args have been passed
        self.cli_args = False

        self.parser = ArgumentParser()
        self.parser.add_argument(
            "-v",
            "--view",
            type=int,
            nargs="?",
            const=-1,
            help="view the note at a given index. Use negatives for recent notes (default is the most recent note)",
        )
        self.parser.add_argument(
            "-n", "--new", help="pass a string to create a new note"
        )
        self.parser.add_argument(
            "-d", "--delete", type=int, help="Delete note at given index"
        )
        self.parser.add_argument(
            "-s",
            "--search",
            help="Enter a string to search for in your notes"
        )

        self.parser.add_argument(
            "--db", action="store_true", help="show the database location"
        )
        self.parser.add_argument(
            "--delete-notes", action="store_true", help="delete all notes on the system"
        )
        self.parser.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="don't print the ascii art on init",
        )

        self.args = self.parser.parse_args()
        self.handle_cli_args()

    def handle_cli_args(self):
        # Turn the args into a dict for easy access to values
        dict_args = vars(self.args)
        # Check for quiet mode so that the logo prints before everything else
        if not dict_args["quiet"]:
            print(random.choice(LOGOS))

        # Check if any args have been provided
        if not any(dict_args.values()):
            return
        # If there are cl args, then the program will terminate after handling them
        # instead of going to normal mode
        self.cli_args = True

        options = {
            "view": self.view,
            "new": self.new,
            "delete": self.delete,
            "search": self.search,
            "db": lambda: print(
                f"Database location: {Colors.GREEN.value} {str(self.database.PATH)} {Colors.WHITE.value}"
            ),
            "delete_notes": self.uninstall,
        }


        # Go through each option. If the option has a value, call the associated function
        for arg in dict_args:
            if dict_args[arg]:
                options[arg]()
        sys.exit()

    def parse_inp(self, inp: str):
        self.inp = inp.split()
        options = {
            "new": self.new,
            "view": self.view,
            "delete": self.delete,
            "exit": self.exit,
            "search": self.search,
            "help": self.help,
            "clear": self.clear,
            "del": self.delete,
            "s" :self.search,
            "c": self.clear,
            "n": self.new,
            "d": self.delete,
            "v": self.view,
            "e": self.exit,
            "h": self.help,
            "q": self.exit,
        }
        # No input, return back
        if len(inp) < 1:
            return

        operation = self.inp[0]
        if operation in options:
            try:
                options[operation]()
            # if user presses ctl-c, cancel the operation
            except KeyboardInterrupt:
                print("\nOperation canceled")
        else:
            print(
                f"Invalid command '{self.inp[0]}'\nType 'help' to get a list of commands"
            )

    def help(self):
        """Print help message"""
        print(
            """
TBNU -- Help Message
Commands:
    (All commands can be shortened to their first letter)
    help                 show this message
    new [note content]   create a new note
    view NOTE NUMBER     view note at the provided number
    search QUERY         search all notes for a provided query
    clear                clear output
    del / delete NOTE NUMBER      delete note at given index
    exit / q             quit the program
            """
        )

    def clear(self) -> None:
        """Clear stdout"""
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def new(self):
        """Make New Note"""

        if self.cli_args:
            note = self.args.new
        else:
            # if the user provided a note after the 'new' command, make that content the note.
            # e.i. 'new hello this is a note' creates a new note
            if len(self.inp) > 1:
                note = " ".join(self.inp[1:])
            else:
                print(
                    "Write your note! Use CTRL-D or CTRL-Z (Windows) to save the note"
                )
                # using sys.stdin.readlines() allows for multiline notes
                note = "".join(sys.stdin.readlines())

        self.database.add(note)
        print("Note created")

    def delete(self):
        """Delete message at index"""
        if self.cli_args:
            i = self.args.delete
        else:
            if len(self.inp) < 2:
                print("Usage: delete <note index number>")
                return

            try:
                i = int(self.inp[1])
            # User inputed an invalid number
            except ValueError:
                return
        note = self.database.delete(i)
        # Some error getting note
        if note is None:
            print(f"Invalid note index '{i}'.")
            return
        print(f"Note #{note.INDEX + 1} has been deleted\n{note.content}")

    def exit(self):
        print("Thank you for using TBNU")
        Database.save(self.database)
        sys.exit()

    def view(self):
        """View note at index"""
        if not self.cli_args:
            if len(self.inp) < 2:
                print("Usage: view <note index number>")
                return
            try:
                i = int(self.inp[1])
            except ValueError:
                return
        else:
            # if not in cli mode, use the index provided on command line
            i = self.args.view

        note = self.database.get(i)
        if note is None:
            print(
                f"Invalid note index {i}. Use a negative number to get your most recent notes"
            )
            return
        print(f"Note #{note.INDEX + 1}\n------\n{note.content}")
    
    def search(self):
        """search within all notes and print the notes that match the search"""
        
        if not self.cli_args:
            if len(self.inp) < 2:
                print("Usage: search <string query>")
            search_query = self.inp[1]
        else:
            search_query = self.args.search
        
        notes = self.database.search(search_query)
        if len(notes) == 0:
            print(f"You have no notes containing '{search_query}' ")

        for note in notes:
            print(f"Note #{note.INDEX + 1} | {note.content[:15]}")

    def uninstall(self):
        if (
            input(
                "Are you sure you want to delete all notes from this system (y/n)\n>> "
            )
            == "y"
        ):
            self.database.PATH.unlink()
            self.database.DIR.rmdir()
            print(
                "Notes have been deleted. Use 'pip uninstall tbnu' to remove the rest of the program"
            )
        else:
            print("Aborted uninstall")