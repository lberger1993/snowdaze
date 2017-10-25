class Participant:
    def __init__(self, id, size, nationality):
        self._id = id
        self._size = size
        self._nationality = nationality

    def get_size(self):
        return self._size

    def get_id(self):
        return self._id
