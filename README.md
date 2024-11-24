# README for The Vegan Meal Game

The Vegan Meal Game is a simple, interactive game built for a vegan friend using **Pygame**, a library that helps create 2D games in Python. In this game, the player controls a veggie character that must avoid non-vegan food items like meat, eggs, and dairy while receiving help from friendly animals. The game features character movement, shooting mechanics, and a score system.

## Game Features

- **Character Movement**: The player controls a veggie character that moves within the screen using the arrow keys.
- **Shooting Mechanism**: The player can shoot "oranges" (acting as projectiles) by pressing the spacebar. These oranges help destroy non-vegan food items.
- **Enemy Items**: The game contains various non-vegan food items like meat, eggs, and dairy, which move across the screen. The player must destroy them to score points.
- **Backup Help**: Randomly appearing animals, such as bees, birds, cows, and hens, assist the player by moving across the screen and helping to clear out non-vegan items.
- **Score System**: The score increases as non-vegan food items are destroyed. Each type of food item adds a different amount to the score.
- **Music and Sound Effects**: Background music plays in a loop, while different sound effects are triggered for actions like shooting and explosions.

## Installation

To run the Vegan Meal Game, ensure you have the following prerequisites installed:

- **Python 3.x**: This game is built using Python 3.
- **Pygame**: The game uses the Pygame library for graphics and sound. Install it by running:

  ```sh
  pip install pygame
  ```

Once you have the prerequisites installed, you can simply run the game by executing the Python script:

```sh
python main.py
```

## File Structure

- **`main.py`**: The main Python script containing the game logic.
- **`sounds/`**: A folder containing sound files used for background music and sound effects.
  - **`background.wav`**: Background music for the game.
  - **`laser.wav`**: Sound effect for shooting.
  - **`explosion.wav`**: Sound effect for explosions.
  - **`horse.wav`**: Sound effect for backup animal help.
- **`pictures/`**: A folder containing images used in the game.
  - **`icon.png`**: The game icon.
  - **`Veggie.png`**: Image of the veggie character.
  - **`meat.png`**: Image of the meat enemy.
  - **`Diary.png`**: Image of the dairy enemy.
  - **`egg.png`**: Image of the egg enemy.
  - **`bee.png, bird.png, cow.png, hen.png, owl.png`**: Images for backup animals.
  - **`Tisch.jpg`**: Background image.
  - **`9ertassa.png`**: Image of the projectile (orange).

## Gameplay Instructions

- **Move the Character**: Use the arrow keys (left, right, up, down) to move your veggie character around the screen.
- **Shoot Projectiles**: Press the spacebar to fire an orange that destroys harmful food items.
- **Avoid Non-Vegan Foods**: Avoid food items like meat, eggs, and dairy. If these items reach the bottom of the screen, you lose.
- **wait for Backup**: Random animals appear to help you in the game.
- **Score**: Your score increases by destroying non-vegan food items. Different items give different points.

## How to Play

- Use the arrow keys to control the veggie character and avoid getting hit by non-vegan food.
- Shoot non-vegan food by pressing the spacebar to shoot oranges.
- Backup animals can be helpful for clearing out food items.
- The game continues until any non-vegan food item reaches the bottom of the screen. When this happens, the game ends and your final score will be displayed.

## Customization

You can customize the game by editing the following parameters:

- **Speed of Enemies**: Change the movement speed of food items by adjusting the values for `meatNewX`, `DiaryNewX`, and `eggNewX`.
- **Speed of Backup Animals**: Adjust the speed of backup animals by changing the `backupnew` variable.
- **Background Music**: You can replace the `background.wav` file with your own background music if you'd like.

## Conclusion

This is a basic Pygame project that demonstrates character movement, collision detection, and interactive elements such as shooting. It was built to be fun and educational, showcasing how to make a simple game in Python using Pygame.

Feel free to customize and expand it to add more features!
