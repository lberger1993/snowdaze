from DatabaseObjects.Accommodation import Accommodation
from DatabaseObjects.Participant import Participant


def return_options(accommodations, group):
    option_matrix = []
    for item in accommodations:
        if group.get_size() <= item.get_capacity() and item.get_availability() is True:
            size_remainder = int(item.get_capacity()) - group.get_size()
            value = {
                'accom_id': item.get_id(),
                'cap': item.get_capacity(),
                'rem': size_remainder,
            }
            if size_remainder == 0:
                item.set_unavailable()
            option_matrix.append(value)
    return option_matrix


if __name__ == "__main__":
    participant = Participant(id=1, size=1, nationality="Germany")
    participant1 = Participant(id=2, size=1, nationality="Germany")
    participant2 = Participant(id=3, size=1, nationality="Germany")
    kolping = Accommodation(accommodation_id=1, capacity=1, bus_stop=10)
    rogers = Accommodation(accommodation_id=2, capacity=1, bus_stop=10)
    high_school = Accommodation(accommodation_id=3, capacity=30, bus_stop=10)
    total_options = list()
    total_options.append(kolping)
    total_options.append(rogers)
    total_options.append(high_school)

    participants = list()
    participants.append(participant)
    participants.append(participant1)
    participants.append(participant2)
    for participant in participants:
        print(return_options(total_options, participant))


