class Guest:
    def __init__(self, name, wallet, song):
        self.name=name
        self.wallet = wallet
        self.favourite_song = song

    def has_enough_money(self):
        return self.wallet
    
    def can_afford(self, amount):
        return self.wallet >= amount

    def can_pay(self, amount):
        self.wallet -= amount

    def cheer(self, songs):
        for song in songs:
            if song.equals(self.favourite_song):
                return "Whoo Hoo!"
        return None

    