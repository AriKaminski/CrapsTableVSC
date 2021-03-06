FILENAME = "CrapsPlayers.csv"
import csv
from pdb import line_prefix
class Player():
    
    def __init__(self, name = "player", balance = 0):
        self.__name = name
        self.__balance = balance
        
    def setName(self, name):
        self.__name = name
    
    
    def setBalance(self, balance):
        self.__balance = balance
        
    def getName(self):
        return self.__name
    
    def getBalance(self):
        return self.__balance
    
    def getStr(self):
        print(self.__name + " (Balance = " + str(self.__balance) + ")" )
        
def display_menu():
    """
    Displays_menu function displays the menu of the various functions to be executed
    """
    print("COMMAND MENU")
    print("list - Display all Players")
    print("add - add a Player")
    print("del - delete a Player")
    print("dep - Make a Deposit")
    

def write_players(players_list):
    with open(FILENAME, 'w') as file:
        for line in file:
            line = line.replace('\n', '')
            players_list.append(line)
    return players_list

def read_players():
    players_list = []
    with open(FILENAME, newline="") as file:
        for line in file:
            line = line.replace("\n", "")
            players_list.append(line)
    return(players_list)


def list(players_list):
    """
    The list function displays the list of Reviews by reviwer username
    """
    
    for i in range(len(players_list)):
        player = players_list[i]
        print(str(i+1) , '.' , player)
    print()


def add(players_list):

    playerName = input("Enter player name")
    playerBalance = int(input("Enter player balance"))
    player = []
    player.append(playerName)
    player.append(playerBalance)
    players_list.append(player)
    write_players(players_list)
    print(playerName , ' was added to the list')


def main():
    print("Welcome to the craps table program")

    players_list = read_players()

    display_menu()
    print()

    command = input("enter command = ")

    while(command.lower() != 'exit'):
        if (command.lower() == 'list'):
            list(players_list)
            display_menu()
        elif (command.lower() == 'add'):
            add(players_list)
            display_menu()
        else:
            print("Invalid command")

        command = input("enter command = ")


if __name__ == "__main__":
    main()

