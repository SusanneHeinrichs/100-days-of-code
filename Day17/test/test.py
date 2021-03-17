class User:
    def __init__(self, name, species):
        self.name = name
        self.art = species
        self.follower = 0



user1 = User("Rudi", "reindeer")

print(user1.name)
