# Asteroid on Steroids

Asteroid on Steroids is a small arcade space shooter built with **Python** and **Pygame**.

The project started as a learning exercise inspired by classic Asteroids-style gameplay, then grew into a more experimental prototype with power-ups, score tracking, lives, dynamic music, and a “mega laser” mechanic.

## Current Features

- Classic asteroid-shooter gameplay
- Player ship with rotation, acceleration, inertia, and screen wrap-around
- Asteroids that spawn from random screen edges
- Asteroids split into smaller asteroids when destroyed
- Bullet shooting with cooldown
- Collision detection between:
  - player and asteroids
  - bullets and asteroids
  - player and power-ups
- Lives and respawn system
- Temporary invincibility after respawn
- Score and persistent high-score tracking
- Random power-up spawning
- Mega laser power-up with rainbow-colored shots
- Basic UI message system
- Dynamic music switching based on score
- Sound effects for shooting, explosions, player hits, and power-up pickup

## Controls

| Key | Action |
|---|---|
| `W` | Thrust forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

## Tech Stack

- Python
- Pygame

## Project Structure

```text
.
├── main.py              # Main game loop, sprite groups, collisions, spawning
├── player.py            # Player movement, shooting, respawn, power-up behavior
├── asteroid.py          # Asteroid object and splitting behavior
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Bullet/projectile logic
├── power_up.py          # Power-up spawning, movement, and drawing
├── circleshape.py       # Shared base class for circular game objects
├── constants.py         # Game constants and tuning values
├── music.py             # Music and sound-effect manager
└── ui/
    └── ui.py            # Score display, high-score file handling, UI messages
```
## How to run

clone the repository:
`git clone https://github.com/Hmimesh/asteroid-on-steroids.git
cd asteroid-on-steroids`

install pygame:
`pip install pygame`

Run the game:
`python main.py`


## Notes:

This is an early prototype and learning project. The core gameplay loop works, but some parts are still rough and are planned for cleanup

Known areas for impovement:

- Replace local absolute sound paths with relative asset paths
- Add a proper start menu and game-over screen
- Refactor global score/lives state into a dedicated game-state object
- Add tests for non-visual logic where possible
- Improve asset loading and error handling
- Add difficulty scaling over time
- Add more enemy and power-up types
- What I Learned

While building this project, I practiced:

- Working with Pygame’s game loop
- Using delta time for frame-rate-independent movement
- Managing sprite groups
- Separating game objects into classes
- Handling collision detection
- Implementing persistent high-score saving
- Building simple UI messages
- Adding sound effects and dynamic music
- Structuring a small game project across multiple files
