from packages import Game as GameModule

def main():
    game = GameModule.Game()
    game.setPlayer()
    game.start()
    

if __name__ == "__main__":
    main()