
class Accommodation:
    def __init__(self, id, capacity, bus_stop):
        self._id = id
        self._capacity = capacity
        self._filter_gender = False
        self._bus_stop = bus_stop

    def get_id(self):
        return self._id

    def get_capacity(self):
        return self._capacity

