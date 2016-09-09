import time
import random

from random import randrange

class Player(object):
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = Board()
        self.location = 0
        self.money = 1500
    def __str__(self):
        return "Player Class for " + str(self.player_name)

    def __repr__(self):
        return "Player Class for " + str(self.player_name)

    def yourturn(self):
        print "It's " + self.player_name + " turn to roll the dice"
        diceOne = randrange(1,6)
        diceTwo = randrange(1,6)
        print self.player_name + " rolled a " + str(diceOne) + " and a " + str(diceTwo)
        time.sleep(2)
        self.location += (diceOne + diceTwo + self.location)
        if self.location >= 40:
            self.location = diceOne + diceTwo
            self.money += 200
        property_landed_on = self.board.property_list[self.location]  # a reference to Property class the player landed pn
        print self.player_name +" landed on " + str(self.board.property_list[self.location])
        if property_landed_on.is_buyable == True:
            self.buy_property()
        time.sleep(2)
        if diceOne == diceTwo:
            self.yourturn()
        if property_landed_on.community_chest:
            self.community_chest_cards()
        if property_landed_on.chance:
            self.chance_cards()
        if self.location and property_landed_on.is_buyable == 'False':
            print "You owe " + self.player_name + property_landed_on.rent
        print str(self.player_name) + " has " + str(self.money)
    def buy_property(self):
        purchase = raw_input("Would you like purchase this property?( Type \"yes\" or no\" )")
        if purchase.lower() == 'yes':
            self.board.property_list[self.location].is_buyable = False
            print "It costs " + str(self.board.property_list[self.location].price)
            if self.money >= self.board.property_list[self.location].price:
                self.money -= self.board.property_list[self.location].price

        else :
            print "You did not purchase"
    def community_chest_cards(self):
        community_chest_random = randrange(1,5)
        if community_chest_random == 1:
            print "Life insurance matures. Collect $100"
            self.money +=100
        if community_chest_random == 2:
            print "Bank error in your favor. Collect $200"
            self.money +=200
        if community_chest_random == 3:
            print "Advance to Go. Collect $200"
            self.money+=200
            self.location = 39
        if community_chest_random == 4:
            print self.player_name + " has won 2nd place at beauty contest. Collect $50"
            self.money +=50
        if community_chest_random == 5:
            print "Christmas fund matures. Collect $100"
            self.money +=100
    def chance_cards(self):
        chance_cards_random = randrange(1,5)
        if chance_cards_random == 1:
            print "Take a ride on the Reading Railroad"
            self.location = 4
        if chance_cards_random == 2:
            print "Go back three spaces"
            self.location -= 3
        if chance_cards_random == 3:
            print "Take a walk on the Boardwalk"
            self.location = 38
        if chance_cards_random ==4:
            print "Bank pays you dividend of $50"
            self.money +=50
        if chance_cards_random == 5:
            print "Pay poor tax of $15"
            self.money-=15
class ComputerPlayer(Player):
    def __str__(self):
        return "Computer Player Class for " + str(self.player_name)

    def __repr__(self):
        return "Computer Player Class for " + str(self.player_name)

    def buy_property(self):
        purchase = randrange(0,6)
        if purchase % 2 == 0:
            print self.player_name + " has purchased this property!"
            self.money -= self.board.property_list[self.location].price
        else:
            print self.player_name + " did not buy this property!"
class Property(object):
    def __init__(self, name, price, is_buyable, community_chest, chance, land_price):
        self.name = name
        self.price = price
        self.owner = ""
        self.is_buyable = is_buyable
        self.community_chest  = community_chest
        self.chance = chance
        self.land_price = land_price
    def __repr__(self):
        return self.name

class Board(object): # only one instance of this
    def __init__(self):
        self.player_list = []  # stores the list of players, in their turn order
        self.property_list = [] # stores a list of properties (instances of Property class)
        self.populate_board()  # make property_list have values

    def add_player(self, player_name):
        self.player_list.append(Player(player_name))

    def add_computer_players(self, num_of_computer_players):
        for _ in range(num_of_computer_players):
            # Run this loop num_of_computer_players time
            random_names = ['Thimble', 'Battleship', 'Shoe', 'Race Car', 'Wheel Barrel']
            self.player_list.append(ComputerPlayer(random.choice(random_names)))

        print self.player_list

    def populate_board(self):
        self.property_list.append(Property("Mediterranean Avenue", 60, True, False, False, 2))
        self.property_list.append(Property("Community Chest", 0, False, True, False, 0))
        self.property_list.append(Property("Baltic Avenue", 60, True, False, False, 4))
        self.property_list.append(Property("Income Tax, lose $100", -100, False, False, False, 0))
        self.property_list.append(Property("Reading Railroad", 200, True, False, False, 0))
        self.property_list.append(Property("Oriental Avenue", 100, True, False, False, 7))
        self.property_list.append(Property("Chance", 0, False, False, True, 0))
        self.property_list.append(Property("Vermont Avenue", 100, True, False, False, 9))
        self.property_list.append(Property("Connecticut Avenue", 120, True, False, False, 10))
        self.property_list.append(Property("just visiting Jail", 0, False, False, False, 0))
        self.property_list.append(Property("St. Charles Place", 140, True, False, False, 12))
        self.property_list.append(Property("Electric Company", 150, True, False, False, 0))
        self.property_list.append(Property("States Avenue", 160, True, False, False, 14))
        self.property_list.append(Property("Virginia Avenue", 160, True, False, False, 14))
        self.property_list.append(Property("Pennsylvania Railroad", 200, True, False, False, 0))
        self.property_list.append(Property("St. James Place", 180, True, False, False, 17))
        self.property_list.append(Property("Community Chest", 0, False, True, False, 0))
        self.property_list.append(Property("Tennessee Avenue", 180, True, False, False, 19))
        self.property_list.append(Property("New York Avenue", 200, True, False, False, 20))
        self.property_list.append(Property("Free Parking", 0, False, False, False, 0))
        self.property_list.append(Property("Kentucky Avenue", 220, True, False, False, 22))
        self.property_list.append(Property("Chance", 0, False, False, True, 0))
        self.property_list.append(Property("Indiana Avenue", 220, True, False, False, 24))
        self.property_list.append(Property("Illinois Avenue", 240, True, False, False,25))
        self.property_list.append(Property("B&O Railroad", 200, True, False, False, 0))
        self.property_list.append(Property("Atlantic Avenue", 260, True, False, False, 27))
        self.property_list.append(Property("Ventnor Avenue", 260, True, False, False, 28))
        self.property_list.append(Property("Water Works", 150, True, False, False, 0))
        self.property_list.append(Property("Marvin Gardens", 280, True, False, False, 30))
        self.property_list.append(Property("Go to Jail", 0, False, False, False, 0))
        self.property_list.append(Property("Pacific Avenue", 300, True, False, False, 32))
        self.property_list.append(Property("North Carolina Avenue", 300, True, False, False, 33))
        self.property_list.append(Property("Community Chest", 0, False, True, False, 0))
        self.property_list.append(Property("Pennsylvania Avenue", 320, True, False, False, 35))
        self.property_list.append(Property("Short Line", 200, True, False, False, 0))
        self.property_list.append(Property("Chance", 0, False, False, True, 0))
        self.property_list.append(Property("Park Place", 350, True, False, False, 38))
        self.property_list.append(Property("Luxury Tax, lose $100", -100, False, False, False, 0))
        self.property_list.append(Property("Boardwalk", 400, True, False, False, 40))
        self.property_list.append(Property("Go, collect $200", 0, False, False, False, 0))

def main():
    global numPlay
    board = Board()
    print "Welcome to Monopoly"
    human_player_name = raw_input("Enter your name: ")
    while True:
        numPlay = input("How many players (Max 4): ")
        if numPlay >=2 and numPlay <=4:
            break
        else:
            numPlay = input("Please enter a valid player number! (2-4)")
    while True:
        startGame = raw_input("Type Start to begin the game: ")
        if startGame.lower() == 'start':
            board.add_player(human_player_name)
            board.add_computer_players(numPlay - 1)
            break
    while True:
        for player in board.player_list:
            player.yourturn()
            time.sleep(2)

main()
