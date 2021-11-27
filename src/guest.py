class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_fee(self, amount):
        self.wallet -= amount

    def check_favourite(self, room):
        if self.favourite_song in room.playlist:
            return "Whoooo!"