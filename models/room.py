class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.till = 0
        self.fee = fee

    def add_to_till(self, amount):
        self.till += amount
    
    def guests_count(self):
        return len(self.guests)
    
    def number_of_songs(self):
        return len(self.songs)

    def get_capacity(self):
        return self.capacity

    def free_spaces(self):
        return self.capacity - len(self.guests)

    def check_in_guests(self, guest):
        if self.free_spaces() >= 0 and guest.can_afford(self.fee):
            guest.can_pay(self.fee)
            self.till += self.fee
            self.guests.append(guest)

    def check_out_guests(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

      