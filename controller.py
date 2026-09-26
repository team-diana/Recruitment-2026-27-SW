def solve(api):
    """
    Your mission: Find the lost shipment (value 2 on the map).
    
    You can use the following methods from the api:
    - api.move_up()     # Returns True if successful, False if blocked
    - api.move_down()
    - api.move_left()
    - api.move_right()
    - api.get_discovered_map() # Returns a 2D list of the map seen so far
                               # -1: Undiscovered, 0: Empty, 1: Obstacle, 2: Shipment
    - api.get_player_pos()     # Returns (x, y) tuple of current position
    - api.process_pygame_events() # Returns a list of pygame events.
    """
    
    while not api.is_game_over():
        # Example of getting the map
        visible_map = api.get_discovered_map()
        px, py = api.get_player_pos()
        
        # TODO: Implement your player controller logic here!
        
        # Query pygame events to keep the window responsive
        events = api.process_pygame_events()
        
        pass
