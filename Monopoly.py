import math
import string
import time
import random

from random import randrange
playerOne = 0
playerTwo = 0
firstChoice = 0
diceNumber = 0
turns = 1
money1 = 1500
money2 = 1500

def chance():
    print "You landed on Chance"
    global money1, money2, turns
    chance = randrange (1,5)
    if chance == 1:
        player1 = 40
        print "Advance to Go"
        print "You have:$ ",money1
    if chance == 2:
        print "Bank pays you dividend of $50"
        money1 += 50
        print "You have:$ ", money1
    if chance == 3:
        print "Advance to St. Charles Place"
        #player1 = 11

    if chance == 4:
        print "Advance to Illinois Ave"
        #player1 = 24
        if chance == 5:
            print "Advance to the nearest Utility"

    #if player1 > 25:
        #player1 = 28;

    #if player1 < 25)
        #player1 = 12
    turns +=1
def communityChest():
    global money1, money2, turns
    print "You landed on Community Chest"
    commChest = randrange (1,5)
    if commChest == 1:
        player1 = 40;
        print "Advance to Go, Collect $200"
        money1+=200
        print "You have:$ ", money1

    if commChest == 2:
        print "From sale of stock you get $50"
        money1 += 50
        print "You have:$ " ,money1


    if commChest == 3:
        print "You have won second prize in a beauty contest, Collect $10"
        money1 += 10
        print "You have:$ ", money1

    if commChest == 4:
        print "Pay school fees of $150"
        money1 -= 150
        print "You have:$ ", money1
    if commChest == 5:
        print "Bank error in your favor, Collect $200"
        money1 += 200
        print "You have:$ ", money1

    turns +=1
def buyProperty(cost):
        global money1
        global money2
    #if turns % 2 == 0:
        purchase = ''
        print "Would you like to buy this property"
        time.sleep(1)
        purchase = raw_input("Type Yes to purchase, type No to not purchase: ")
        if (purchase.lower() == 'yes'):
            print "You have purchased this property!"
            time.sleep(1)
            money1 -= cost
            print "You have:$ " ,money1
        else:
            print "You did not purchase this property."
            print "You have:$ ", money1
def landPropertiesPlayerOne():
    global turns, playerOne, money1
    if playerOne == 1:
        medAve = 60
        print name ,"landed on Mediterranean Avenue($60)"
        time.sleep(1)
        buyProperty(medAve)
        turns +=1
    if playerOne == 2:
        communityChest()
    if playerOne == 3:
        balticAve = 60
        print name, "landed on Baltic Avenue($60)"
        time.sleep(1)
        buyProperty(balticAve)
        turns +=1
    if playerOne == 4:
        print name, "landed on Income Tax, pay $200"
        money1 -= 200
        print "You have:$ ", money1
        turns +=1
    if playerOne == 5:
        readRail = 200
        print name, "landed on Reading Railroad($200)"
        time.sleep(1)
        buyProperty(readRail)
        turns +=1
    if playerOne == 6:
        orientalAve = 100
        print name, "landed on Oriental Ave($100)"
        time.sleep(1)
        buyProperty(orientalAve)
        turns +=1
    if playerOne == 7:
        chance()
    if playerOne == 8:
        vermontAve = 100
        print name, "landed on Vermont Avenue($100)"
        time.sleep(1)
        buyProperty(vermontAve)
        turns +=1
    if playerOne == 9:
        connectAve = 120
        print name,"landed on Connecticut Avenue($120)"
        time.sleep(1)
        buyProperty(connectAve)
        turns +=1
    if playerOne == 10:
        print name, "are just visiting jail"
        turns +=1
    if playerOne == 11:
        charlesPlace = 140
        print name, "landed on St. Charles Place($140)"
        time.sleep(1)
        buyProperty(charlesPlace)
        turns +=1
    if playerOne == 12:
        elecCompany = 150
        print name,"landed on Electric Company($150)"
        time.sleep(1)
        buyProperty(elecCompany)
        turns +=1
    if playerOne == 13:
        statesAve = 160
        print name, "landed on States Avenue($160)"
        time.sleep(1)
        buyProperty(statesAve)
        turns +=1
    if playerOne == 14:
        virginiaAve = 160
        print name,"landed on Virginia Avenue($160)"
        time.sleep(1)
        buyProperty(virginiaAve)
        turns +=1
    if playerOne == 15:
        pennRail = 200
        print name,"landed on Pennsylvania Avenue($200)"
        time.sleep(1)
        buyProperty(pennRail)
        turns +=1
    if playerOne == 16:
        jamesPlace = 180
        print name,"landed on St. James Place($180)"
        time.sleep(1)
        buyProperty(jamesPlace)
        turns +=1
    if playerOne == 17:
        communityChest()
    if playerOne == 18:
        tennesseeAve = 180
        print name,"landed on Tennessee Avenue($180)"
        time.sleep(1)
        buyProperty(tennesseeAve)
        turns +=1
    if playerOne == 19:
        nyAve = 200
        print name, "landed on New York Avenue($200)"
        time.sleep(1)
        buyProperty(nyAve)
        turns +=1
    if playerOne == 20:
        print name, "landed on Free Parking, you get $500"
        money1+=500
        print "You have:$", money1
    if playerOne == 21:
        kentuckAve = 220
        print name, "landed on Kentucky Avenue($220)"
        time.sleep(1)
        buyProperty(kentuckAve)
        turns +=1
    if playerOne == 22:
        chance()
    if playerOne == 23:
        indianaAve = 220
        print name, "landed on Indiana Avenue($220)"
        time.sleep(1)
        buyProperty(indianaAve)
        turns +=1
    if playerOne == 24:
        illinoisAve = 240
        print name, "landed on Illinois Avenue($240)"
        time.sleep(1)
        buyProperty(illinoisAve)
        turns +=1
    if playerOne == 25:
        boRailroad = 200
        print name, "landed on B&O Railroad($200)"
        time.sleep(1)
        buyProperty(boRailroad)
        turns +=1
    if playerOne== 26:
        atlanticAve = 260
        print name, "landed on Atlantic Avenue($260)"
        time.sleep(1)
        buyProperty(atlanticAve)
        turns +=1
    if playerOne == 27:
        ventnorAve = 260
        print name, "landed on Ventnor Avenue($260)"
        time.sleep(1)
        buyProperty(ventnorAve)
        turns+=1
    if playerOne == 28:
        waterWorks = 150
        print name,"landed on Water Works($150)"
        time.sleep(1)
        buyProperty(waterWorks)
        turns += 1
    if playerOne == 29:
        marvinGardens = 280
        print name,"landed on Marvin Gardens($280)"
        time.sleep(1)
        buyProperty(marvinGardens)
        turns += 1
    if playerOne  == 30:
        print "Go to the Jail"
    if playerOne == 31:
        pacificAve = 300
        print name,"landed on Pacific Avenue($300)"
        time.sleep(1)
        buyProperty(pacificAve)
        turns += 1
    if playerOne == 32:
        nocarAve = 300
        print name,"landed on North Carolina Avenue($300)"
        time.sleep(1)
        buyProperty(nocarAve)
        turns += 1
    if playerOne == 33:
        communityChest()
    if playerOne == 34:
        pennAve = 320
        print name,"landed on Pennsylvania Avenue($320)"
        time.sleep(1)
        buyProperty(pennAve)
        turns +=1
    if playerOne == 35:
        shortLine = 200
        print name,"landed on Short Line($200)"
        time.sleep(1)
        buyProperty(shortLine)
        turns +=1
    if playerOne == 36:
        chance()
    if playerOne == 37:
        parkPlace = 350
        print name,"landed on Park Place($350)"
        time.sleep(1)
        buyProperty(parkPlace)
        turns +=1
    if playerOne == 38:
        print name, "landed on Luxury Tax, lose $100"
        money1-=100
    if playerOne == 39:
        boardwalk = 400
        print name, "landed on Boardwalk($400)"
        time.sleep(1)
        buyProperty(boardwalk)
        turns+=1
    if playerOne == 40:
        print name,"landed on Go, collect $400"
        money1+=400
    if playerOne > 40:
        playerOne = 0
def playerOneTurn():
    global playerOne
    if playerOne <40:
        print "It's",name, "turn to roll"
    diceNumber = randrange(1,12)
    #diceNumber = 1
    playerOne += diceNumber
    if playerOne < 40:
        print "Your landed on: ", playerOne
        time.sleep(1)

    landPropertiesPlayerOne()


def goesFirst():
    global turns
    #rollOne = randrange(1, 12)
    #rollTwo = randrange(1,12)
    #if rollOne > rollTwo :
    while (turns > 0):
     playerOneTurn()
        #turns = 2

def main():
   global name
   print "Welcome to Monopoly"
   name = raw_input("Enter your name: ")
   startGame = raw_input("Type Start to begin the game: ")
   if startGame == 'Start':
     goesFirst()
   elif startGame == 'start':
     goesFirst()
   else :
      main()




main()