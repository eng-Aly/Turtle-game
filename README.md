## Running the Game

1. **Launch the TurtleSim Node**:
after running roscore
   Start the `turtlesim_node`:
   ```bash
   rosrun turtlesim turtlesim_node
   ```

2. **Run the Game Engine (Observer Node)**:
   The observer node tracks player health and controls the game:
   ```bash
   rosrun game observer.py
   ```

3. **Run the Turtle Controllers**:
   Each player runs their own turtle controller node. Replace `turtle1` with the name of your turtle (e.g., `turtle2`, `turtle3`), by default its turtle1:
   ```bash
   rosrun game controller.py __name:=turtle1
   ```

   Each player controls their turtle using keyboard inputs:
   - `w`: Move forward
   - `s`: Move backward
   - `a`: Turn left
   - `d`: Turn right
   - `q`: Attack any player in range of 2 unites

4. **Monitor the Game**:
   The observer node will print the winner who last to the end.

## Game Rules

- **Attacking**: Players can attack other turtles using the `q` key. If a turtle is within a distance of `2.0` units, it will lose `50` health points.
- **Health**: Each turtle starts with `100` health points. If a turtle's health drops to `0`, it is eliminated from the game.
- **Winning**: The last turtle standing is declared the winner!
