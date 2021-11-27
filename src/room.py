class Room:
    def __init__(self, name, playlist, capacity, fee):
        self.name = name
        self.playlist = playlist
        self.capacity = capacity
        self.fee = fee
        self.guests = []
        self.takings = 0.0

    def count_guests(self):
        return len(self.guests)

    def remaining_capacity(self):
        return (self.capacity - self.count_guests())

    def add_takings(self, amount):
        self.takings += amount

    def add_guest(self, guest):
        if self.remaining_capacity() > 0:
            if guest.can_afford(self.fee):
                self.guests.append(guest)
                guest.pay_fee(self.fee)
                self.add_takings(self.fee)
                return guest.check_favourite(self)
            else:
                return "Sorry, you don't have enough money."
        else:
            return "Sorry, room's all full!"

    def remove_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
        else:
            return "Guest not found" 

    def count_songs(self):
        return len(self.playlist)

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            return "Song not in playlist" 