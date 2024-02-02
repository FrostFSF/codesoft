from random import randint
from colorama import Fore, init, Style
import os

class Format:
    def __init__(self) -> None:
        self.grey = Fore.LIGHTBLACK_EX
        self.blue = Fore.LIGHTBLUE_EX
        self.default = Fore.WHITE
        self.green = Fore.LIGHTGREEN_EX
        self.purple = Fore.LIGHTMAGENTA_EX

class Console:
    def clear(self):
        os.system("cls")

def checkCondition(player, comp):
    if(player["move"] == comp["move"]):
        return {'winner': 'none', 'points': 0}
    elif(player["move"] + comp["move"] == 4):
        if(comp["move"] < player["move"]):
            return {'winner': 'comp', 'points': 1}
        else:
            return {'winner': 'player', 'points': 1}
    elif(player["move"] + comp["move"] == 3):
        if(comp["move"] > player["move"]):
            return {'winner': 'comp', 'points': 1}
        else:
            return {'winner': 'player', 'points': 1}
    else:
        if(comp["move"] > player["move"]):
            return {'winner': 'comp', 'points': 1}
        else:
            return {'winner': 'player', 'points': 1}
# 1-r,2-p,3-s
        
class Game: 
    def __init__(self) -> None:
        self.players = {
            'comp': {
                'score': 0
            },
            'player': {
                'score': 0
            }
        }
        self.round = 5
        self.format = Format()
        self.console = Console()

    def computerChoice(self):
        return randint(1,3)
    
    def defineMove(self,move):
        if(move == 1):
            return 'Rock'
        elif(move == 2):
            return 'Paper'
        elif(move == 3):
            return 'Scissors'
    
    def decidedWinner(self):
        if(self.players["player"]["score"] > self.players["comp"]["score"]):
            return {'winner': 'player'}
        return {
            'winner': 'computer'
        }
    
    def resetGame(self):
        self.players['comp']['score'] = 0
        self.players['player']['score'] = 0
        self.round = 5


    def start(self):
        currentRound = 1
        userChoice = 0
        end = False
        while(currentRound <= self.round and not end):
            print(f'Player Score: {self.format.blue}{self.players["player"]["score"]}{self.format.default} \t\tComputer Score: {self.format.green}{self.players["comp"]["score"]}{self.format.default}')
            print("\nPlease choose an option")
            print("1) Rock")
            print("2) Paper")
            print("3) Scissors")
            userChoice = int(input("Enter your choice: "))
            if(userChoice == 1):
                self.console.clear()
                compChoice = self.computerChoice()
                result = checkCondition({'move':userChoice},{'move':compChoice})
                if(result['winner'] != 'none'):
                    self.players[result['winner']]['score'] += 1
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')
                    currentRound += 1
                else:
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')

            elif(userChoice == 2):
                self.console.clear()
                compChoice = self.computerChoice()
                result = checkCondition({'move':userChoice},{'move':compChoice})
                if(result['winner'] != 'none'):
                    self.players[result['winner']]['score'] += 1
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')
                    currentRound += 1
                else:
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')
            elif(userChoice == 3):
                self.console.clear()
                compChoice = self.computerChoice()
                result = checkCondition({'move':userChoice},{'move':compChoice})
                if(result['winner'] != 'none'):
                    self.players[result['winner']]['score'] += 1
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')
                    currentRound += 1
                else:
                    print(f'{"*"*50}\nPlayer Move: {self.format.blue}{self.defineMove(userChoice)}{self.format.default}\t\tComputer Move: {self.format.green}{self.defineMove(compChoice)}{self.format.default}\n{"*"*50}')
            else:
                self.console.clear()
                print("Invalid option")
        
        print(f'Player Score: {self.format.blue}{self.players["player"]["score"]}{self.format.default} \t\tComputer Score: {self.format.green}{self.players["comp"]["score"]}{self.format.default}')
        print(f'And the winner is: {self.format.purple}{self.decidedWinner()["winner"]}{self.format.default}!')

        gameEnd = input("Do you want to play again? (y or press any button to continue): ")
        if(gameEnd == 'y'):
            end = False
            self.resetGame()
        else:
            end = True
            

game = Game()
game.start()
