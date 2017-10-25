
class Accommodation:
    def __init__(self, accommodation_id, capacity, bus_stop):
        self._accommodation_id = accommodation_id
        self._capacity = capacity
        self._filter_gender = False
        self._bus_stop = bus_stop
        self._is_available = True

    def get_id(self):
        return self._accommodation_id

    def get_capacity(self):
        return self._capacity

    def get_availability(self):
        return self._is_available

    def set_unavailable(self):
        return self._is_available is False




