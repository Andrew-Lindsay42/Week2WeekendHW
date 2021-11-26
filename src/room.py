class Room:
    def __init__(self, name, playlist):
        self.name = name
        self.playlist = playlist
        self.guests = []

    def count_guests(self):
        return len(self.guests)

    def add_guest(self, guest):
        self.guests.append(guest)