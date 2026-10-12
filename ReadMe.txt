# Tic-Tac-Toe

A classic Tic-Tac-Toe game built with Python and Flask. Play the familiar two-player game through a web interface, taking turns placing Xs and Os on a 3×3 grid to try to get three in a row.

## Features

- **Interactive Game Board:** Play using a 3×3 grid.
- **Turn-Based Gameplay:** Alternate between X and O.
- **Win Detection:** Identify winning combinations across rows, columns, and diagonals.
- **Draw Detection:** Recognise when the board is full without a winner.
- **Game Logic:** Prevent invalid moves and manage the progression of a game.

## Technologies

- Python
- Flask
- HTML
- CSS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SinceSlicedBread/tic-tac-toe.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tic-tac-toe
   ```

3. Install Flask:

   ```bash
   pip install Flask
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Open the local URL displayed in your terminal in a web browser.

## How to Play

1. Start a new game.
2. Players take turns selecting an empty square.
3. The first player to place three matching symbols in a row, column, or diagonal wins.
4. If all nine squares are filled without a winner, the game ends in a draw.

## Purpose

This project demonstrates Python programming, game-state management, conditional logic, web application development, and the use of Flask to connect backend logic with a user interface.