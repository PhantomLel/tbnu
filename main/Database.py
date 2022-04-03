import pickle
import math
from main.Note import Note

class Database:
    PATH = 'main/db.pkl'
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
        # This reduces the absoulute value of the index by one
        index = int(math.copysign(abs(index)-1, index))

        return self._notes[index].content

    @staticmethod
    def save(database):
        with open(database.PATH, 'wb') as f:
            pickle.dump(database, f)