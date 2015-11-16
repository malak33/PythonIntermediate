from collections import namedtuple, deque

passenger = namedtuple('passenger', 'name seat priority')

passengers = [
    passenger('Bob', '1A', True),
    passenger('Sally', '14A', False),
    passenger('Fred', '21B', False),
    passenger('Ed', '17D', False),
    passenger('Tim', '13C', False),
    passenger('Nancy', '1C', True),
    passenger('Cole', '2A', True),
    passenger('Herb', '11A', False),
    passenger('Steve', '19A', False),
    passenger('David', '21A', False)
]

boarding_line = deque()

for passenger in passengers:
    if passenger.priority:
        boarding_line.appendleft(passenger)
    else:
        boarding_line.append(passenger)

while boarding_line:
    name, seat, priority = boarding_line.popleft()
    print('Name: {name:10} Seat: {seat}'.format(name=name, seat=seat))
