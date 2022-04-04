TBNU 
==
Terminal Based Notes Utility!
-----

TBNU is a super easy to use notes program. Takes no time to set up and has simple use.

## Features
- Write down whatever very quickly
- Thats literally it

## How to Use
The normal interface can be used as such:
```bash
$ tbnu    
-- TBNU notes --

TBNU -- Help Message
Commands:
    (All commands can be shortened to their first letter)
    help                 show this message
    new [note content]   create a new note
    view NOTE NUMBER     view note at the provided number
    exit / q             quit the program
            
>> new note
Note created
>> view 1 
Note #1
------
note
>> exit
Thank you for using TBNU
$ 
```

You can also use it directly from the command line:
```bash
$ tbnu -n "first note"
-- TBNU notes --
Note created
$ tbnu -v
-- TBNU notes --
Note #1
------
first note
$ tbnu -n "2nd note"
-- TBNU notes --
Note created
$ tbnu -v 2
-- TBNU notes --
Note #2
------
2nd note
$ 
```

To remove all note use:
```bash
$ tbnu --uninstall
-- TBNU notes --
Are you sure you want to delete all notes from this system (y/n)
>> y
Notes have been deleted. Use 'pip uninstall tbnu' to remove the rest of the program
```
