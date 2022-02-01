#This is a Craps Table simulation game
#Author - Ari Kaminski
#Version 1.1 - working table with limited betting

import random

class Player():
    
    def __init__(self, name = "player", balance = 0):
        self.__name = name
        self.__balance = balance
        
    def setName(self):
        self.__name = name
    
    
    def setBalance(self):
        self.__balance = balance
        
    def getName(self):
        return self.__name
    
    def getBalance(self):
        return self.__balance
    
    def getStr(self):
        print(self.__name + " (Balance = " + str(self.__balance) + ")" )
        
    def winner(self, d):
        self.__balance = self.__balance + d
        return self.__balance
    
    def loser(self, w):
        self.__balance = self.__balance - w
        return self.__balance

    def bigWinner(self, d):
        self.__balance = self.__balance + d
        return self.__balance
    
    def bigLoser(self, w):
        self.__balance = self.__balance - w
        return self.__balance
        


def rollDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    return total

def main():
    name = input("What is your name? = ")
    
    Player1 = Player(name, 100)
    Player1.getStr()
    
    keepPlaying = 'yes'
    
    while keepPlaying == "yes" or keepPlaying == "y" or keepPlaying == "Y":
        bet = int(input("How much would you like to bet? "))
        comeOut = True
        while comeOut == True:
            point = rollDice()
            if (point == 2 or point == 3 or point == 12):
                Player1.loser(bet)
                print(point, "Craps! Your balance is", Player1.getBalance())
                break
            elif (point == 7 or point == 11):
                Player1.winner(bet)
                print(point, "Winner! Your balance is", Player1.getBalance())
                break
            elif (point == 4 or point == 5 or point == 6 or point == 8 or point == 9 or point == 10):
                print("The point is :", point)
                comeOut = False
                backBet = int(input("Enter amount for back bet = "))
                while comeOut == False:
                    x = rollDice()
                    if (x == 4 or 10):
                        print(x,"Big Winner!")
                        backBet = backBet + (2 * backBet)
                        bet = bet + backBet
                        Player1.winner(bet)
                        break
                    elif (x == 5 or 9):
                        print(x,"Big Winner!")
                        backBet = backBet + (3/2 * backBet)
                        bet = bet + backBet
                        Player1.winner(bet)
                    elif (x == 6 or 8):
                        print(x,"Big Winner!")
                        backBet = backBet + (7/6 * backBet)
                        bet = bet + backBet
                        Player1.winner(bet)
                    elif (x == 7):
                        print(x,"out, Loser!")
                        Player1.loser(bet)
                        break
                    else:
                        print(x)
                        rollDice()
            else:
                rollDice()
        Player1.getStr()
        keepPlaying = input("Would you like to play again? (y / n) = ")
    print("Thanks for playing! Your balance is", Player1.getBalance())
    if (Player1.getBalance() > 100):
        print("You beat the house!")
    else:
        print("Better luck next time!")
        
        
            
        
if __name__ == "__main__":
    main()
    
    
    
    