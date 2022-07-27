import pickle
from pathlib import Path
from tbnu.Note import Note
from appdirs import user_data_dir


class Database:
    # Get the location of the data dir
    DIR = Path(user_data_dir(appname='tbnu', version="0.1.4"))
    DIR.mkdir(parents=True, exist_ok=True)
    # This is the actual path to the file
    PATH = DIR / "db.pkl"

    def __init__(self) -> None:
        self._notes = []
        self.current_index = 0
        self.new = True

    def validate_index(self, index) -> int:
        """Fix the given index"""
        # make sure the index isnt out of bounds
        if abs(index) > len(self._notes) or index == 0:
            return
            # If the index is negative then it stays the same. Otherwise subtract one from it
            # This is important because negative indices start at -1 e.g. -1 returns last item and -2 returns 2nd last item.
            # Positive indices start at 0, so if user passes in 1, it needs to be turned into 0.
        return index if index < 0 else index - 1

    def add(self, note):
        """Add note object to database"""
        # add the note with the proper index
        self._notes.append(Note(note, self.current_index))
        self.current_index += 1
        Database.save(self)

    def delete(self, index) -> Note:
        """Delete note at given index and return the deleted note"""
        index = self.validate_index(index)
        if index is None:
            return
        note = self._notes.pop(index)
        Database.save(self)
        return note

    def get(self, index):
        # make sure the index isnt out of bounds
        index = self.validate_index(index)
        # if the index is invalid
        if index is None:
            return
        return self._notes[index]
    
    def search(self, query):
        return list(filter(lambda note: query in note.content, self._notes))

    @staticmethod
    def save(database):
        database.new = False
        with Database.PATH.open("wb") as f:
            pickle.dump(database, f)

    @staticmethod
    def load():
        with Database.PATH.open("rb") as f:
            return pickle.load(f)
