# Tetris

This repository is a Python implementation of the classic Tetris game, using the Pygame library for graphics and user interaction.

## Demo
![Tetris Demo](https://github.com/mihaiapostol14/Tetris/blob/7a309f65776b039a850f2bc86a42ef4d15ea664d/assets/demo.gif)

to play the game. Use arrow keys to control the pieces.

---


## Features

- **Classic Tetris Gameplay**: Implements falling tetromino pieces (I, J, L, O, S, T, Z shapes) that can be moved, rotated, and locked into place.
- **Line Clearing**: Automatically clears completed lines and updates the playing field.
- **Game Over Detection**: The game ends when new pieces cannot be placed at the top of the grid.
- **Keyboard Controls**: Supports arrow-key controls for moving and rotating tetrominos.
- **Simple UI**: Displays the grid and colored tetrominos using Pygame's rendering capabilities.
- **Configurable Parameters**: Constants like window size, block size, and colors are defined at the top of `main.py` for easy customization.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) (see `requirements.txt` for version)
- Additional dependencies: asgiref, sqlparse, tzdata (though these are not directly used by the game, they are included in `requirements.txt`)

## How It Works

- The game starts by creating a window and initializing the game grid.
- New tetromino pieces are randomly generated and descend automatically.
- Players use the keyboard to move pieces left/right, rotate, or accelerate their drop.
- When a piece reaches the bottom or lands on another, it locks into the grid.
- Complete lines are cleared, and points are scored (basic line clearing is implemented).
- The game loop continues until no more pieces can be placed.

## Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/Tetris.git
cd Tetris
```

### 2. Create and Activate a Virtual Environment

**Install Python**

If you don't have Python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of Python. Then you can check your version of Python using the command lines below:

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run Game

```bash
python main.py
```

## File Overview

- **main.py**: Contains all game logic, including the `Tetris` class (manages game state, drawing, input, etc.) and the `Tetromino` class (piece shapes, rotation, and position).
- **requirements.txt**: Lists required Python packages.


This project is a simple and educational example of game development with Python and Pygame. It is ideal for learning about event loops, rendering, and basic game logic.