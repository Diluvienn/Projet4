
class Film:
    def __init__(self, name):
        self.name = name

    def watch (self, player):
        print("Bon visionnage")

class FilmCassette(Film):
    def __init__(self, name):
        self.name = name
        self.magnetic_tape = True

    def rewind(self):
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

    def watch(self, player):
        if player.type != "cassette":
            print ("mauvas lecteur")
        else:
            print("Ca commence !")
        super().watch(player)

class Player:
    def __init__(self, type):
        self.type = type

if __name__ == "__main__":
    # film = ("2001")
    film_cassette = FilmCassette("Oh")
    print(film_cassette.name)
    player = Player("cassette")
    film_cassette.watch(player)
