class Room:
    def __init__(self, name, playlist):
        self.name = name
        self.playlist = playlist
        self.guests = []

    def count_guests(self):
        return len(self.guests)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
        else:
            return "Guest not found" 

    def count_songs(self):
        return len(self.playlist)

    def add_song(self, song):
        self.playlist.append(song)