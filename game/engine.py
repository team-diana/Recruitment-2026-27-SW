import pygame
import os
from .map_generator import generate_map

# Constants
CELL_SIZE = 40
GRID_WIDTH = 20
GRID_HEIGHT = 15
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FOG_RADIUS = 3
MOVE_DELAY_MS = 100

# Colors for fallback
COLOR_FOG = (0, 0, 0)
COLOR_FLOOR = (200, 200, 200)
COLOR_WALL = (100, 100, 100)
COLOR_PLAYER = (0, 0, 255)
COLOR_PACKAGE = (255, 215, 0)
COLOR_GRID = (50, 50, 50)

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Operation Hartsfield - Customs Depot Search")
        
        # Grid layout: 0=Empty, 1=Obstacle, 2=Target
        self.grid, self.player_pos, self.target_pos = generate_map(GRID_WIDTH, GRID_HEIGHT, obstacle_prob=0.3)
        
        # Discovery map: False = undiscovered, True = discovered
        self.discovered = [[False for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
        
        self.game_over = False
        self.success = False
        
        # Load assets
        self.assets = self._load_assets()
        
        # Set window icon
        if self.assets['player']:
            pygame.display.set_icon(self.assets['player'])
        
        self.update_fog_of_war()
        self.draw()

    def _load_assets(self):
        assets = {}
        base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
        
        # Helper to load, scale and conditionally remove white fringe
        def load_image(name, fallback_color, transparent=True, scale=1.0):
            path = os.path.join(base_path, name)
            if os.path.exists(path):
                try:
                    target_size = int(CELL_SIZE * scale)
                    img = pygame.image.load(path).convert()
                    img = pygame.transform.scale(img, (target_size, target_size))
                    
                    if transparent:
                        # Create a magenta colorkey
                        COLORKEY = (255, 0, 255)
                        
                        # Remove near-white fringe by turning it into colorkey
                        for x in range(target_size):
                            for y in range(target_size):
                                color = img.get_at((x, y))
                                if color.r > 230 and color.g > 230 and color.b > 230:
                                    img.set_at((x, y), COLORKEY)
                        img.set_colorkey(COLORKEY)
                        
                    return img
                except Exception as e:
                    print(f"Error loading {name}: {e}")
            return None

        assets['player'] = load_image('player.jpg', COLOR_PLAYER, transparent=True, scale=1.4)
        assets['obstacle'] = load_image('obstacle.jpg', COLOR_WALL, transparent=True)
        assets['package'] = load_image('package.jpg', COLOR_PACKAGE, transparent=True)
        assets['floor'] = load_image('floor.jpg', COLOR_FLOOR, transparent=False)
        
        return assets

    def update_fog_of_war(self):
        px, py = self.player_pos
        for dx in range(-FOG_RADIUS, FOG_RADIUS + 1):
            for dy in range(-FOG_RADIUS, FOG_RADIUS + 1):
                # Using Manhattan distance or Chebyshev. Chebyshev (square) is simpler.
                if abs(dx) <= FOG_RADIUS and abs(dy) <= FOG_RADIUS:
                    nx, ny = px + dx, py + dy
                    if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                        self.discovered[nx][ny] = True

    def move_player(self, dx, dy) -> bool:
        if self.game_over:
            return False
            
        nx, ny = self.player_pos[0] + dx, self.player_pos[1] + dy
        
        # Check bounds
        if not (0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT):
            return False
            
        # Check obstacles
        if self.grid[nx][ny] == 1:
            return False
            
        # Move
        self.player_pos = (nx, ny)
        self.update_fog_of_war()
        
        # Check win
        if self.player_pos == self.target_pos:
            self.game_over = True
            self.success = True
            
        self.draw()
        
        # Process some events to keep window responsive and handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                return False
                
        # Delay for animation feel
        pygame.time.delay(MOVE_DELAY_MS)
        return True

    def get_visible_grid(self) -> list[list[int]]:
        visible_grid = [[-1 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.discovered[x][y]:
                    visible_grid[x][y] = self.grid[x][y]
        return visible_grid

    def draw(self):
        self.screen.fill(COLOR_FOG)
        
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                if self.discovered[x][y]:
                    # Draw floor
                    if self.assets['floor']:
                        self.screen.blit(self.assets['floor'], rect)
                    else:
                        pygame.draw.rect(self.screen, COLOR_FLOOR, rect)
                    
                    # Draw content
                    cell_val = self.grid[x][y]
                    if cell_val == 1:
                        if self.assets['obstacle']:
                            self.screen.blit(self.assets['obstacle'], rect)
                        else:
                            pygame.draw.rect(self.screen, COLOR_WALL, rect)
                    elif cell_val == 2:
                        if self.assets['package']:
                            self.screen.blit(self.assets['package'], rect)
                        else:
                            pygame.draw.rect(self.screen, COLOR_PACKAGE, rect)
                            
                    # Grid lines
                    pygame.draw.rect(self.screen, COLOR_GRID, rect, 1)
                else:
                    # Undiscovered
                    pygame.draw.rect(self.screen, COLOR_FOG, rect)
                    pygame.draw.rect(self.screen, COLOR_GRID, rect, 1)
        
        # Draw player
        px, py = self.player_pos
        rect = pygame.Rect(px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if self.assets['player']:
            player_w, player_h = self.assets['player'].get_size()
            offset_x = (CELL_SIZE - player_w) // 2
            offset_y = (CELL_SIZE - player_h) // 2
            draw_rect = pygame.Rect(px * CELL_SIZE + offset_x, py * CELL_SIZE + offset_y, player_w, player_h)
            self.screen.blit(self.assets['player'], draw_rect)
        else:
            pygame.draw.rect(self.screen, COLOR_PLAYER, rect)
            
        # Draw game over message
        if self.game_over:
            font = pygame.font.SysFont(None, 48)
            msg = "MISSION ACCOMPLISHED!" if self.success else "GAME OVER"
            color = (0, 255, 0) if self.success else (255, 0, 0)
            text = font.render(msg, True, color)
            
            # Draw semi-transparent background
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            
            text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            self.screen.blit(text, text_rect)
            
        pygame.display.flip()

