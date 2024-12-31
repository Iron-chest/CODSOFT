# Tic-Tac-Toe AI

This repository contains a Python implementation of an unbeatable AI agent for the classic game of Tic-Tac-Toe. The AI uses the **Minimax algorithm** to ensure optimal moves and a challenging gameplay experience for human players.

## Features
- **Unbeatable AI**: The AI employs the Minimax algorithm to always make the best possible move.
- **Interactive Gameplay**: Play against the AI in an intuitive command-line interface.
- **Human-Friendly**: Easy-to-follow code and instructions for customization or learning purposes.

## How It Works
### Core Concepts:
1. **Game State Representation**:
   - The board is represented as a list of 9 elements, where each element corresponds to a cell on the Tic-Tac-Toe grid.

2. **Minimax Algorithm**:
   - The algorithm evaluates possible moves to determine the optimal play for the AI, minimizing potential losses.

3. **Win Conditions**:
   - Horizontal, vertical, and diagonal alignments of the same symbol (X or O).

### Code Breakdown:
#### 1. **Initialization**:
```python
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # X is the human player
        self.ai_player = 'O'  # O is the AI player
```
- Initializes the game board as an empty 3x3 grid.
- Sets `X` as the human player and `O` as the AI player.

#### 2. **Board Display**:
```python
def print_board(self):
    """Prints the current state of the board."""
```
- Outputs the current state of the game board for the player.

#### 3. **Win Checking**:
```python
def check_winner(self):
    """Checks if there is a winner."""
```
- Evaluates all possible win conditions (rows, columns, diagonals).

#### 4. **Full Board Check**:
```python
def is_board_full(self):
    """Checks if the board is full."""
```
- Determines if all cells on the board are occupied, indicating a draw if no winner exists.

#### 5. **Minimax Algorithm**:
```python
def minimax(self, depth, is_maximizing):
    """Minimax algorithm to determine the best move."""
```
- Implements the recursive algorithm to evaluate the best moves for the AI.
- Scores are assigned as follows:
  - `+10` for AI wins.
  - `-10` for human wins.
  - `0` for draws.

#### 6. **Finding the Best Move**:
```python
def find_best_move(self):
    """Finds the best move for the AI using Minimax."""
```
- Iterates over all possible moves to determine the optimal play for the AI.

#### 7. **Gameplay Loop**:
```python
def play_game(self):
    """Main game loop."""
```
- Alternates turns between the human and AI players.
- Ends when there is a winner or the board is full.

## How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```
2. Run the game:
   ```bash
   python3 tic_tac_toe.py
   ```
3. Enter your moves by specifying a number (1-9) corresponding to the grid:
   ```
   1 | 2 | 3
   --|---|---
   4 | 5 | 6
   --|---|---
   7 | 8 | 9
   ```
4. Try to beat the AI (Good luck!)

## Project Structure
- `tic_tac_toe.py`: The main script containing the game logic.

## Learning Outcomes
- Understand basic **game theory** and **search algorithms**.
- Learn to implement the Minimax algorithm for decision-making.
- Practice Python programming through a fun project.

## Acknowledgments
- This project was inspired by the desire to understand and implement game theory principles.

---
Have fun playing Tic-Tac-Toe and exploring the code.

