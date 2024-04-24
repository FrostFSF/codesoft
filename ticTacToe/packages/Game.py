from packages import Player as PlayerModule
from colorama import Fore, init, Style
import os

init(autoreset=False)

class Game:
    def __init__(self):
        self._tiles = 9
        self._board = [[],[],[]]
        self._end = False
        self._initializeBoard()

    #for initializing the board
    def _initializeBoard(self):
        position = 1
        for i in range(1,4):
            for j in range(0,3):
                self._board[ i - 1 ].append(position)
                position += 1

    #for setting the player
    def setPlayer(self):
        playerName = input("Enter the player name: ")
        playerSymbol = input("Enter player symbol ( X / O ): ")
        
        if(playerSymbol != 'X' or playerSymbol != 'O'):
            playerSymbol = 'X'

        self.playerOne = PlayerModule.Player(playerName, playerSymbol)

        if(playerSymbol == "X"):
            playerSymbol = "O"
        else:
            playerSymbol = "X"

        playerName = input("Enter the player name: ")
        self.playerTwo = PlayerModule.Player(playerName, playerSymbol)

    def switch(self,playerObject):
        if(playerObject.symbol == 'X'): #X symbol we want to return O
            if(self.playerOne.symbol == 'O'):
                return self.playerOne
            return self.playerTwo
        else:   #O symbol we want to return X
            if(self.playerOne.symbol == 'X'):
                return self.playerOne
            return self.playerTwo
        
    def clearScreen(self):
        os.system("cls")

    def setSymbolColor(self, playerObject):
        if(playerObject.symbol == 'X'):
            return Fore.LIGHTBLUE_EX
        return Fore.LIGHTGREEN_EX
    
    def convertBool(self, userInput):
        if(userInput.title() == 'Y'):
            return True
        return False
    
    def placeInBoard(self,board, player, position):
        if(position <= 3 and position >= 1):
            if(type(self._board[0][position - 1]) == str):
                return False
            self._board[0][position - 1] = player.symbol
            self._tiles -= 1
            return True
        elif(position <= 6 and position >= 4):
            if(type(self._board[1][position - 4]) == str):
                return False
            self._board[1][position - 4] = player.symbol
            self._tiles -= 1
            return True
        elif(position <= 9 and position >= 7):
            if(type(self._board[2][position - 7]) == str):
                return False
            self._board[2][position - 7] = player.symbol
            self._tiles -= 1
            return True
        return False



    def checkHorizontally(self,playerSymbol):
        pass

    def checkVertically(self, playerSymbol):
        pass

    def checkDiagonally(self, playerSymbol):
        pass

    def resetGame(self):
        self.__init__()

    def rematch(self):
        rematch = input("Do you want a rematch? : ")
        rematch = self.convertBool(rematch)
        #if yes reset board and just continue
        if(rematch):
            self.resetGame()
            return True
        return False

    def start(self):
        player = self.playerOne
        symbolColor = self.setSymbolColor(player)
        defaultColor = Fore.WHITE

        while(self._tiles != 0):
            self.clearScreen()
            print(f'Current Player: {symbolColor}{player.symbol}{defaultColor}')
            self.printBoard()
            position = int(input("Enter the position: "))
            #place the mark in board
            ifPlaced = self.placeInBoard(self._board, player, position)

            while(not ifPlaced):
                print("The place is already marked!")
                position = int(input("Enter the new position: "))
                ifPlaced = self.placeInBoard(self._board, player, position)


            #check if that player has won after placing the mark
            if(self.checkHorizontally(player.symbol) or self.checkVertically(player.symbol) or self.checkDiagonally(player.symbol)):
                self.clearScreen()
                self.printBoard()
                print(f'>>> {Fore.MAGENTA}{player.name} HAS WON THE MATCH!{Fore.WHITE} <<<')
                #ask for rematch?
                if(self.rematch()):
                    pass
                #else they just don't want to play the game and they want to exit therefore 
                else:
                    print("Thank you for playing!")
                    break
            elif(self._tiles == 0):
                self.clearScreen()
                self.printBoard()
                print("Looks like no one won!")
                if(self.rematch()):
                    pass
                else:
                    print("Thank you for playing!")
                    break

            else:
                player = self.switch(player)
                symbolColor = self.setSymbolColor(player)


    #for printing the board
    def printBoard(self):
        for i in range(0,3):
            print("[",end="")
            for j in range(0,3):
                if(self._board[i][j] == 'X'):
                    print(f' {Fore.LIGHTBLUE_EX}{self._board[i][j]}{Fore.WHITE} ', end="")
                elif(self._board[i][j] == 'O'):
                    print(f' {Fore.LIGHTGREEN_EX}{self._board[i][j]}{Fore.WHITE} ', end="")
                else: 
                    print(f' {self._board[i][j]} ', end="")
            print("]")