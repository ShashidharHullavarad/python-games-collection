# Snake Game 🐍

A classic Snake game built with Python and Pygame!

## Features

- 🎮 Classic snake gameplay
- 🍎 Collect red food to grow longer
- 📊 Score tracking
- 🔄 Auto-restart when you hit yourself
- ⌨️ Arrow key controls

## Installation

1. Install the required dependency:
```bash
pip install pygame
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python snake_game.py
```

2. **Controls:**
   - ⬆️ **UP Arrow** - Move up
   - ⬇️ **DOWN Arrow** - Move down
   - ⬅️ **LEFT Arrow** - Move left
   - ➡️ **RIGHT Arrow** - Move right

3. **Objective:**
   - Eat the red food to grow longer
   - Each food gives you 10 points
   - Don't run into yourself!
   - The snake wraps around the screen edges

## Game Rules

- The snake starts at a random position moving in a random direction
- Collect red food blocks to increase your score and length
- If the snake's head touches its body, the game resets
- Your score is displayed in the top-left corner

## Technical Details

- **Window Size:** 800x600 pixels
- **Grid Size:** 20x20 pixels per cell
- **Frame Rate:** 10 FPS
- **Colors:**
  - Snake: Green
  - Food: Red
  - Background: Black
  - Grid: White

## Requirements

- Python 3.x
- Pygame library

Enjoy the game! 🎮
