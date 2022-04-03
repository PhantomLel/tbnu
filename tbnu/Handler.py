import sys

class Handler:
    def __init__(self, argv : sys.argv, database) -> None:
        self.argv = argv
        self.database = database
    
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
        pass

    def new(self):
        """Make New Note"""
        
        # if the user provided a note after the 'new' command, make that content the note.
        # e.i. 'new hello this is a note' creates a new note 
        if len(self.inp) > 1:
            self.database.add(' '.join(self.inp[1:]))
        else:
            print("Write your note! Use CTRL-D or CTRL-Z (Windows) to save the note")
            # using sys.stdin.readlines() allows for multiline notes
            note = ''.join(sys.stdin.readlines())
            self.database.add(note)
        print('Note created')

    def exit(self):
        print("Thank you for using TBNU")

        sys.exit()

    def view(self):
        """View note"""
        if len(self.inp) < 2:
            print("Usage: view <note index number>")
            return
        
        try:
            i = int(self.inp[1])
        except ValueError:
            return

        note = self.database.get(i)
        if not note:
            print(f"Invalid note index {i}. Use a negative number to get your most recent notes")
            return
        print(note)