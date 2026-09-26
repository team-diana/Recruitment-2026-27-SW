# Operation Hartsfield

Year 3023. Team DIANA has finally landed in the USA, ready to take part in URC. Everything seems to be fine, until... a hologram from Alpha Starlines! Due to an unfortunate series of events, it seems the rover has been lost in shipment, and is located somewhere in the depths of Hartsfield spaceport in Atlanta. Without hesitation, Vincenzo is selected to teleport on-site and retrieve the package. After several close calls, he manages to infiltrate the customs depot disguised as a local officer. Now, he must navigate the vast, unfamiliar warehouse to secure the rover. The pressure is on: will he successfully locate the lost shipment, or will he soon find himself frantically trying to justify his failure to the "Dark Lord" himself, Stefano?

## Instructions
You are provided with a complete Python 2D game engine that simulates an airport customs depot. Your objective is to design a player controller that can navigate the environment, discover the hidden areas, and find the lost shipment.

The environment is generated procedurally and features a fog of war. You cannot see the entire map at the beginning; you only see what is immediately around your character.

To interact with the game, you must complete the `solve(api)` function inside `controller.py`. You are provided with the `api` object which exposes the following methods:
* `api.move_up()`: Moves the character one cell up (returns `True` if successful, `False` if blocked).
* `api.move_down()`: Moves the character one cell down.
* `api.move_left()`: Moves the character one cell left.
* `api.move_right()`: Moves the character one cell right.
* `api.get_discovered_map()`: Returns a 2D list of integers (`list[list[int]]`) representing the map you have explored so far. 
  * `0`: Empty, walkable floor
  * `1`: Concrete wall (obstacle)
  * `2`: The lost shipment (target)
  * `-1`: Undiscovered fog of war
* `api.get_player_pos()`: Returns your current position as an `(x, y)` tuple.
* `api.is_game_over()`: Returns `True` if you have found the shipment.
* `api.process_pygame_events()`: Returns a list of pygame events. Call this in your loops to handle keyboard/mouse inputs and prevent the game window from freezing.

You have complete freedom on how to build this controller. A simple solution could be just creating a controller to manually move the character. However, more creative, articulated and autonomous solutions are highly favored! You can try anything. ANYTHING.

You are free to define any additional classes or functions inside `controller.py`. You aren't allowed to modify `engine.py`, `map_generator.py`, or `api.py`.

**Setup:**

Run `make configure` to install the requirements in a virtual environment. (Windows users without `make` can run `configure.bat`)

Run `make run` to execute the game and test your controller. (Windows users without `make` can run `run.bat`)

## Expected outputs
Provide the completed version of `controller.py` containing your player controller, and an `instructions.txt` file containing an explanation of your controller and how to use it.

## Challenge's score
Total score: 500
