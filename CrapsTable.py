#This is a Craps Table simulation game
#Author - Ari Kaminski
#Version 1.2 - Working pass line betting with backbet. Bets rounded down on decimal payout

import random
import math
#import dicerollergui

class Player(): #This is the player object class
   
    def __init__(self, name = "player", balance = 100):     #Creates a player, name and balance parameters
        self.__name = name
        self.__balance = balance
       
    def setName(self, name):        #Name Setter
        self.__name = name
   
    def setBalance(self, balance):
        self.__balance = balance
       
    def getName(self):
        return self.__name
   
    def getBalance(self):
        return self.__balance
   
    def getStr(self):
        print(self.__name + " (Balance = $" + str(self.__balance) + ")" )                    # Prints user name and user balance
       
    def winner(self, d):                                    # Updates balance with user bet when winning a comeout roll or hitting a point when comeOut = false
        self.__balance = self.__balance + d                 
        return self.__balance
   
    def loser(self, w):                                     # Updates balance with user bet when losing a comeout roll or 7-out when comeOut = false
        self.__balance = self.__balance - w
        return self.__balance

#def diceGUI():
    #dicerollergui.roll_dice()

def rollDice():                                             #rolldice() simulates the rolling of dice
    die1 = random.randint(1,6)                              #Rolls a single die between 1-6
    die2 = random.randint(1,6)                              
    total = die1 + die2                                     #Total of both single rolls above 
    return total                                            #Returns die1 + die2

def main():
    name = input("What is your name? = ")                   #User input for name
   
    Player1 = Player(name, 100)                             #Creates Player object with given name parameter and 100 starting bankroll
    Player1.getStr()        
   
    keepPlaying = 'yes'                                     # How I decided to control the main game loops below
   
    while keepPlaying == "yes" or keepPlaying == "y" or keepPlaying == "Y":             #Start of main loop, ends if player does not enter y
        if (Player1.getBalance() <= 1):                                                 #Ends main loop if player attempts to play with 0 dollars
            print("You ran out of money!")
            break
        bet = int(input("How much would you like to bet? $ "))                            # First pass line bet, start of game

        comeOut = True                                                                  # comeOut starts the comeout roll, first phase of game
        while comeOut == True:                                                          # comeOut roll gameplay loop. Operates one time
            point = rollDice()                                                          # sets point equal to rollDice()
            if (point == 2 or point == 3 or point == 12):                               # Craps, losing bet if playing pass line
                Player1.loser(bet)                                                      # Subtracts the users bet from player balance
                print(point, "Craps! Your balance is $ ", Player1.getBalance())
                break
            elif (point == 7 or point == 11):                                           # Winner, pays 1 to 1 based on user pass line bet.
                Player1.winner(bet)                                                     # Adds the users winnings to player balance
                print(point, "Winner! Your balance is $ ", Player1.getBalance())
                break
            elif (point == 4 or point == 5 or point == 6 or point == 8 or point == 9 or point == 10):       # Sets a point for phase 2
                print("The point is :", point)
                comeOut = False                                                         # Stops phase 1, setting the above while loop to false
                if((Player1.getBalance() - bet) <= 0): 
                    print("You do not have enough for backbet")
                    backBet = 0
                else:
                    print("Your balance is currently = $",(Player1.getBalance() - bet))
                    backBet = int(input("Enter amount for back bet = $ "))
                while comeOut == False:                                                 # Start of phase 2, the rolling phase
                    x = rollDice()                                                      # This rolls dice until a point is hit or 7-out
                    if (x == point):                                                    # If point is hit, big winner and breaks loop.
                        print(x, "Big Winner!")
                        if(point == 4 or point == 10):                                  # If point is 4 or 10 and hit, pays bet + backbet(multiplier)
                            backBet = backBet + (2 * backBet)                           # Sets value for backbet payout
                            bet = bet + backBet                                         # adds backbet payout to original bet
                        elif(point == 5 or point == 9):             
                            backBet = backBet + (3/2 * backBet)                         
                            bet = bet + backBet                                     
                        elif(point == 6 or point == 8):
                            backBet = backBet + (7/6 * backBet)
                            bet = bet + backBet                                         # Needs to notice if backbet has a decimal and round down
                        bet = bet // 1                                                  # Takes the modified bet and rounds down to nearest int, as the casino would
                        Player1.winner(bet)
                        break
                    elif (x == 7):                                                      # 7 out, player loses passline bet and original bet
                        bet = bet + backBet                                             # sets bet equal to comeout bet + backbet
                        print(x,"out, Loser!")
                        Player1.loser(bet)                                              # Deducts bet from player balance
                        break
                    else:                                                               # Continues the loop until point or 7 is rolled
                        print(x)
                        rollDice()
            else:
                rollDice()
        Player1.getStr()
        keepPlaying = input("Would you like to play again? (y / n) = ")                 # Tracks player input so loop is not infinite
    print("Thanks for playing! Your balance is $", Player1.getBalance())                # End of game message, displays player balance
    if (Player1.getBalance() > 100):                                                    # Checks if player balance is higher than starting balance
        print("You beat the house!")
    else:                                                                               # checks if player balance is lower than starting balance
        print("Better luck next time!")
               
       
if __name__ == "__main__":          # Main method call
    main()