"""
Notebook
"""
import note

class Notebook:
    """
    Notebook main class
    """
    notes = []
    def new_note(self, memo: str, tags=''):
        """
        Create a new note.
        """
        tags = tags.split(', ')
        new_note = note.Note(memo, tags)
        self.notes.append(new_note)

    def search(self, s_filter: str)-> list:
        """
        Search note by tags
        """
        possible_notes = []
        for note1 in self.notes:
            if s_filter in note1.tags:
                note_id = self.notes.index(note1)
                possible_notes.append((note_id, note1.memo))
        return possible_notes

    def modify_memo(self, note_id, memo):
        """
        Modify memo to the note with note id
        """
        note_id = int(note_id)
        if note_id > len(self.notes):
            return "There is no such id"
        self.notes[note_id].memo = memo

    def modify_tags(self, note_id, tags):
        """
        Modify tags to the note with note id
        """
        note_id = int(note_id)
        if note_id > len(self.notes):
            return "There is no such id"
        tags = tags.split(', ')
        self.notes[note_id].tags = tags
