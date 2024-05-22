class Room:
    def __init__(self, name, size, capacity, room_type):
        self.name = name
        self.size = size
        self.capacity = capacity
        self.room_type = room_type

class Group:
    def __init__(self, name, num_students, category, preferred_room_type=None):
        self.name = name
        self.num_students = num_students
        self.category = category
        self.preferred_room_type = preferred_room_type


def assign_rooms(groups, rooms):
    assigned_rooms = []

    # Sort rooms by capacity in descending order
    rooms.sort(key=lambda x: x.capacity, reverse=True)
    # print('all rooms', len(rooms))

    for group in groups:
        # Filter rooms based on specification
        if group.preferred_room_type:
            available_rooms = [room for room in rooms if room.room_type == group.preferred_room_type]
        else:
            available_rooms = rooms

        if not available_rooms:
            if group.category == "arts":
                available_rooms = [room for room in rooms if room.room_type != "Science Lab"]
            else:
                available_rooms = [room for room in rooms if room.room_type == "Science Lab"]

        # Sort available rooms by capacity
        available_rooms.sort(key=lambda x: x.capacity, reverse=True)
        print('availabel rooms', len(available_rooms))

        # Assign the first available room with enough capacity
        room_assigned = False
        for room in available_rooms:
            if room.capacity >= group.num_students and room not in assigned_rooms:
                print(f"Assigning room {room.name} to group {group.name}")
                assigned_rooms.append(room)
                room_assigned = True
                break

        if not room_assigned:
            print(f"No suitable room found for group {group.name}")
        else:
            continue

    # check for any free rooms
    remaining_rooms = [room for room in rooms if room not in assigned_rooms]

    return remaining_rooms

# Sample data
rooms = [
    Room("Room1", 50, 100, "Classroom"),
    Room("Room2", 30, 89, "Science Lab"),
    Room("Room3", 40, 100, "Classroom"),
    Room("Room4", 50, 50, "Lab")
]

groups = [
    Group("Group1", 25, "science"),
    Group("Group2", 35, "arts", "Lab"),
    Group("Group3", 40, "science", "Science Lab")
]

# Assign rooms to groups
remaining_rooms = assign_rooms(groups, rooms)

# Handle any remaining rooms
if remaining_rooms:
    print("Some rooms were left unassigned:", [room.name for room in remaining_rooms])
