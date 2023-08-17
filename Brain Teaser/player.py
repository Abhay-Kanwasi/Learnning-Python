# Guess the output 

class Player:
    # Number of player in the game
    count = 1
    new = 2

    def __init__(self, name):
        self.name = name
        self.count += 1


p1 = Player('Parzival')
print(Player.count) # Output : 1
print(Player.new)  # Ouptut : 2