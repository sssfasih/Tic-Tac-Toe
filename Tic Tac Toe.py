"""
Tic Tac Toe;
by Syed Fasih Uddin (19B-029-SE) - 20/6/2020
Email: sssfasih@gmail.com
"""

# counter for Max 2 players exception
counter = 0
# listing all suits to avoid Illegal moves
all_suits = []


class Suit():
    def __init__(self, suit):
        global counter
        global all_suits
        self.suit = suit
        all_suits.append(self.suit)
        counter += 1
        if counter > 2:
            print("No more then 2 players can play Tic Tac Toe!")
        else:
            print(f"Player {counter} has joined the game")


class Player(Suit):

    def __init__(self, Suit):
        super().__init__(Suit)
        # print(self.suit)

    def move(self, suit, number):

        if suit not in all_suits:
            print(" \n ILLEGAL MOVE: WRONG SUIT \n")
        elif (number) < 1 or (number) > 9:
            print("\n ILLEGAL MOVE:", number, "is OUT OF BOARD! \n")

        elif self.board[number - 1] == None:
            self.board[number - 1] = suit
            print(suit, "Placed at", number)
            print("Current Scenerio:")
            print(self.board[0:3])
            print(self.board[3:6])
            print(self.board[6:9], "\n")

        else:
            print("Current Scenerio:")
            print(self.board[0:3])
            print(self.board[3:6])
            print(self.board[6:9], "\n")
            print("ILLEGAL MOVE: Someone has already placed there")


class Game(Player):
    def __init__(self, Player1, Player2):
        super().__init__(Player1)
        super().__init__(Player2)
        self.board = []
        for i in range(3):
            for j in range(3):
                self.board.append(None)
        print("Current Scenerio:")
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9], "\n")


# -------------- PLAY AREA -----------------------
# Defining the suits of Players: "X" and "O"
G = Game("X", "O")

# Playing game row wise - output is on screen
G.move("X", 1)
#G.move("O", 1)
#G.move("X",10)
G.move("O", 9)
G.move("X", 5)
