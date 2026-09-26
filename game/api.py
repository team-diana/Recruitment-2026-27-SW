import pygame

class CustomsAPI:
    def __init__(self, engine):
        self._engine = engine
        
    def move_up(self) -> bool:
        """Move the character one cell up. Returns True if successful, False if blocked."""
        return self._engine.move_player(0, -1)
        
    def move_down(self) -> bool:
        """Move the character one cell down. Returns True if successful, False if blocked."""
        return self._engine.move_player(0, 1)
        
    def move_left(self) -> bool:
        """Move the character one cell left. Returns True if successful, False if blocked."""
        return self._engine.move_player(-1, 0)
        
    def move_right(self) -> bool:
        """Move the character one cell right. Returns True if successful, False if blocked."""
        return self._engine.move_player(1, 0)
        
    def get_discovered_map(self) -> list[list[int]]:
        """
        Returns a 2D matrix representing the discovered map.
        0 = Empty cell
        1 = Obstacle
        2 = Target (Missing Package)
        -1 = Undiscovered cell (Fog of War)
        """
        return self._engine.get_visible_grid()
        
    def get_player_pos(self) -> tuple[int, int]:
        """Returns the (x, y) tuple of the player's current position."""
        return self._engine.player_pos
        
    def is_game_over(self) -> bool:
        """Returns True if the game is over (package found or quit)."""
        return self._engine.game_over
        
    def process_pygame_events(self):
        """
        Helper method to query the pygame events.
        """
        import sys
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self._engine.game_over = True
                pygame.quit()
                sys.exit(0)
        return events
