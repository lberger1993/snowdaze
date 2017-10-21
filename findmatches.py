from DatabaseObjects.Accommodation import Accommodation
from DatabaseObjects.Participant import Participant


def return_options(accommodations, group):
    option_matrix = []
    for item in accommodations:
        if group.get_size() <= item.get_capacity():
            value = {
                'accom_id': item.get_id(),
                'cap': item.get_capacity(),
                'rem': int(item.get_capacity()) - group.get_size()
            }
            option_matrix.append(value)
    return option_matrix


if __name__ == "__main__":
    participant = Participant(id=1, size=30, nationality="Germany")
    kolping = Accommodation(id=1, capacity=20, bus_stop=10)
    rogers = Accommodation(id=2, capacity=10, bus_stop=10)
    high_school = Accommodation(id=3, capacity=30, bus_stop=10)
    total_options = []
    total_options.append(kolping)
    total_options.append(rogers)
    total_options.append(high_school)

    print(return_options(total_options, participant))

