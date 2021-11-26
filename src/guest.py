class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_entry(self):
        self.wallet -= 5