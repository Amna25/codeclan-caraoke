class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.till = 0
        self.fee = fee
      