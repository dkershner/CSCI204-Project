''' Dan Kershner
    This file has the document stream error class which is simply an error used
    in the document stream class.
'''
class DocumentStreamError(Exception):
    def __init__(self, data):
        self.data = data
