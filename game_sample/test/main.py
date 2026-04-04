import GameEngine

W, H = 1200, 800
FPS = 60

if __name__ == "__main__":
    game = GameEngine.GameEngine((W, H), FPS)
    game.run()
    
    
