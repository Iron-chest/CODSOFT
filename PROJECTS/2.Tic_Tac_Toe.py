import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # X is the human player
        self.ai_player = 'O'  # O is the AI player

    def print_board(self):
        """Prints the current state of the board."""
        print("\n")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]} ")
            if i < 2:
                print("---|---|---")
        print("\n")

    def check_winner(self):
        """Checks if there is a winner."""
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def is_board_full(self):
        """Checks if the board is full."""
        return ' ' not in self.board

    def minimax(self, depth, is_maximizing):
        """Minimax algorithm to determine the best move."""
        winner = self.check_winner()
        
        if winner == self.ai_player:
            return 10 - depth
        elif winner == self.current_player:
            return depth - 10
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.ai_player
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.current_player
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        """Finds the best move for the AI using Minimax."""
        best_score = float('-inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.ai_player
                score = self.minimax(0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        
        return best_move

    def play_game(self):
        """Main game loop."""
        while True:
            # Print the board
            self.print_board()
            
            # Check for a winner or full board before player's turn
            if (winner := self.check_winner()) is not None:
                print(f"{winner} wins!")
                break
            if self.is_board_full():
                print("It's a draw!")
                break
            
            # Human player's turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if move < 0 or move > 8 or self.board[move] != ' ':
                        raise ValueError("Invalid move. Try again.")
                    break
                except ValueError as e:
                    print(e)

            # Update board with human's move
            self.board[move] = self.current_player
            
            # Check for a winner after human's turn
            if (winner := self.check_winner()) is not None:
                self.print_board()
                print(f"{winner} wins!")
                break
            
            # Check for a full board after human's turn
            if self.is_board_full():
                print("It's a draw!")
                break
            
            # AI player's turn
            ai_move = self.find_best_move()
            if ai_move is not None:
                self.board[ai_move] = self.ai_player
            
# Start the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
