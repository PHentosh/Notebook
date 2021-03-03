"""
Note
"""
from datetime import date

class Note:
    """
    Note class
    """

    def __init__(self, memo, tags):
        """
        init func
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()

    def match(self, serch_filter):
        """
        Func for searching. Return True if serch_filter is in tags, 
        else False.
        """
        if serch_filter in self.tags:
            return True
        else:
            return False
