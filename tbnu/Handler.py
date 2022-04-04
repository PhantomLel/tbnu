import sys
from argparse import ArgumentParser
from tbnu.Database import Database

class Handler:
    def __init__(self, argv : sys.argv, database) -> None:
        self.argv = argv
        self.database = database
        # Tracks if any cli args have been passed
        self.cli_args = False

        self.parser = ArgumentParser()
        self.parser.add_argument(
            '-v', '--view',
            type=int,
            nargs='?',
            const=-1,
            help='view the note at a given index. Use negatives for recent notes (default is the most recent note)'
            )
        self.parser.add_argument(
            '-n', '--new',
            help="pass a string to create a new note"
        )

        self.parser.add_argument(
            '--db',
            action='store_true',
            help="show the database location"
        )
        self.parser.add_argument(
            '--uninstall',
            action='store_true',
            help="uninstall TBNU from the system"
        )

        self.args = self.parser.parse_args()
        self.handle_cli_args()

    
    def handle_cli_args(self):
        # Turn the args into a dict for easy access to values
        dict_args = vars(self.args)
        # Check if any args have been provided
        if not any(dict_args.values()):
            return
        
        self.cli_args = True
        options = {
            "view" : self.view,
            "new" : self.new,
            "db" : lambda: print("Database location: " + str(self.database.PATH)),
            "uninstall" : self.uninstall
        }
        # Go through each option. If the option has a value, call the associated function
        for arg in dict_args: 
            if dict_args[arg]:
                options[arg]()
        sys.exit()

    
    def parse_inp(self, inp : str):
        self.inp = inp.split()
        options = {
            "new" : self.new,
            "view" : self.view,
            "exit" : self.exit,
            "help" : self.help,
            "n" : self.new,
            "v" : self.view,
            "e" : self.exit,
            "h" : self.help,
            "q" : self.exit
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
            print(f"Invalid command '{self.inp[0]}'\nType 'help' to get a list of commands")
    
    def help(self):
        print(
            """
TBNU -- Help Message
Commands:
    (All commands can be shortened to their first letter)
    help                 show this message
    new [note content]   create a new note
    view NOTE NUMBER     view note at the provided number
    exit / q             quit the program
            """
        )

    def new(self):
        """Make New Note"""

        if self.cli_args:
            note = self.args.new
        else:
            # if the user provided a note after the 'new' command, make that content the note.
            # e.i. 'new hello this is a note' creates a new note 
            if len(self.inp) > 1:
                note = ' '.join(self.inp[1:])
            else:
                print("Write your note! Use CTRL-D or CTRL-Z (Windows) to save the note")
                # using sys.stdin.readlines() allows for multiline notes
                note = ''.join(sys.stdin.readlines())
        
        self.database.add(note)
        print('Note created')

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
        if not note:
            print(f"Invalid note index {i}. Use a negative number to get your most recent notes")
            return
        print(f"Note #{note.INDEX + 1}\n------\n{note.content}")
    
    def uninstall(self):
        if input("Are you sure you want to delete all notes from this system (y/n)\n>> ") == "y":
            self.database.PATH.unlink()
            self.database.DIR.rmdir()
            print("Notes have been deleted. Use 'pip uninstall tbnu' to remove the rest of the program")
        else:
            print("Aborted uninstall")