#!/usr/bin/python
import sys
import pickle
from tbnu.Database import Database
from tbnu.Handler import Handler

def main():
    try:
        with open(Database.PATH, 'rb') as f:
            database = pickle.load(f)
            database.new = False
    except FileNotFoundError:
        database = Database()
        Database.save(database)

    print('-- TBNU notes --')

    if database.new:
        print("help msg")

    handler = Handler(sys.argv, database)
    while True:
        try:
            inp = input('>> ')
            handler.parse_inp(inp) 
        except KeyboardInterrupt:
            print("\nType 'exit' to exit the program")

if __name__ == '__main__':
    main()