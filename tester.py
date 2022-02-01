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
        
    # def comeOutWinner(self, d):
    #     self.__balance = self.__balance + d
    #     return self.__balance
    
    # def comeOutLoser(self, w):
    #     self.__balance = self.__balance - w
    #     return self.__balance

    def bigWinner(self, d):
        self.__balance = self.__balance + d
        return self.__balance
    
    def bigLoser(self, w):
        self.__balance = self.__balance - w
        return self.__balance

    
    


