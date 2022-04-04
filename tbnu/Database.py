import math
import pickle
from pathlib import Path
from tbnu.Note import Note
from appdirs import user_data_dir

class Database:
    # Get the location of the data dir
    DIR = Path(user_data_dir(appname='tbnu', version="0.1.0"))
    DIR.mkdir(parents=True, exist_ok=True)
    # This is the actual path to the file
    PATH = DIR / 'db.pkl'
    def __init__(self) -> None:
       self._notes = []
       self.new = True

    def add(self, note):
        """Add note object to database"""
        # add the note with the proper index
        self._notes.append(Note(note, len(self._notes)))
        Database.save(self)

    def get(self, index):
        # make sure the index isnt out of bounds
        if abs(index) > len(self._notes) or index == 0:
            return 
        
        if index < 0:
            pass
        else:
            index -=1

        return self._notes[index]

    @staticmethod
    def save(database):
        database.new = False
        with Database.PATH.open('wb') as f:
            pickle.dump(database, f)
    
    @staticmethod
    def load():
        with Database.PATH.open('rb') as f:
            return pickle.load(f)