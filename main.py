import pygame
from game import GameEngine, CustomsAPI
from controller import solve

def main():
    # Initialize the engine
    engine = GameEngine()
    
    # Create the API wrapper
    api = CustomsAPI(engine)
    
    # Start the controller
    try:
        solve(api)
    except Exception as e:
        print(f"Error in controller: {e}")
        
    # Keep the window open if the game ended successfully or if solve() exited
    while not engine.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.game_over = True
        pygame.time.delay(100)
        
    # Wait a bit after game over before closing
    pygame.time.delay(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
