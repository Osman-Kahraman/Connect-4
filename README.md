# Connect 4 Game in Python

This repository contains a Python implementation of the classic Connect 4 game, playable in the console. The game allows two players (X and O) to take turns dropping pieces into a grid, with the goal of forming a horizontal, vertical, or diagonal line of four consecutive pieces. It features an automatic save and load system to keep track of the game state between sessions.

### Features:
- **Dynamic UI**: The game displays a simple, visually appealing grid in the console.
- **Autosave/Autoload**: Game progress is automatically saved in a `memory.json` file, allowing players to resume their game later.
- **Win celebration**: The game includes a fun celebration sequence with animated fireworks when a player wins.
- **Permission handling**: Ensures the smooth execution of the game by safely handling moves and memory management.

### Requirements:
- Python 3.x

### Usage:
Clone the repository and run the game in your terminal:
```bash
python connect_4.py
```
