class Queue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def enqueue(self, val):
        self.size += 1
        self.storage.append(val)

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None


class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, val):
        self.size += 1
        self.storage.append(val)

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop()
        else:
            return None


reverse_dirs = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}


class Graph:

    """Represent the world as a dictionary of rooms mapping (room, dir) as edge."""

    def __init__(self):
        self.rooms = {}

    def add_vertex(self, room):
        """
        Add a vertex to the graph.
        """
        if room not in self.rooms:
            self.rooms[room] = {d: '?' for d in room.get_exits()}

    def go_in_direction_until_dead_end(self, room, direction, path=None):
        if path == None:
            path = []
        if direction in room.get_exits():
            next_room = room.get_room_in_direction(direction)
            path.append(direction)
            self.rooms[room][direction] = next_room
            self.rooms[next_room][reverse_dirs[direction]] = room
            return self.go_in_direction_until_dead_end(next_room, direction, path)
        else:
            return path

    def get_unexplored_dir(self, room):
        return [direction for direction, value in self.rooms[room].items() if value == '?']