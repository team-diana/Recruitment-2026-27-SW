import random
from collections import deque

def generate_map(width, height, obstacle_prob=0.3):
    """
    Generates a map of size width x height.
    Returns: grid, start_pos, target_pos
    grid: 2D list where 0=empty, 1=obstacle, 2=target
    start_pos: (x, y) tuple
    target_pos: (x, y) tuple
    """
    while True:
        # Initialize empty grid
        grid = [[0 for _ in range(height)] for _ in range(width)]
        
        # Place obstacles
        for x in range(width):
            for y in range(height):
                if random.random() < obstacle_prob:
                    grid[x][y] = 1
                    
        # Pick start and target positions
        start_pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        target_pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        
        # Ensure they are far enough apart
        dist = abs(start_pos[0] - target_pos[0]) + abs(start_pos[1] - target_pos[1])
        if dist < (width + height) // 2:
            continue
            
        grid[start_pos[0]][start_pos[1]] = 0
        grid[target_pos[0]][target_pos[1]] = 2
        
        # Verify reachability using BFS
        if _is_reachable(grid, start_pos, target_pos, width, height):
            return grid, start_pos, target_pos

def _is_reachable(grid, start_pos, target_pos, width, height):
    queue = deque([start_pos])
    visited = set([start_pos])
    
    while queue:
        cx, cy = queue.popleft()
        
        if (cx, cy) == target_pos:
            return True
            
        # Check neighbors
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited and grid[nx][ny] != 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    return False
