import sys
from tbnu.Handler import Handler
from tbnu.Database import Database

def main():
    # if the data dir exists and the db has already been created, load it
    if Database.PATH.exists():
        database = Database.load()
    else:
        database = Database()
        
    print('-- TBNU notes --')

    handler = Handler(sys.argv, database)
    # If the database is new, print the help message
    if database.new:
        handler.help()

    while True:
        try:
            inp = input('>> ')
            handler.parse_inp(inp) 
        except KeyboardInterrupt:
            print("\nType 'exit' to exit the program")

if __name__ == '__main__':
    main()