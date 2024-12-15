import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), None)  # Create a 3x3 board initialized with None
        self.current_player = 'X'  # Human player is 'X'
        self.ai_player = 'O'  # AI player is 'O'

    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print(" | ".join([' ' if cell is None else cell for cell in row]))
            print("-" * 9)

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != None:
                return self.board[i, 0]
            if self.board[0, i] == self.board[1, i] == self.board[2, i] != None:
                return self.board[0, i]
        
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != None:
            return self.board[0, 0]
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != None:
            return self.board[0, 2]

        return None if None in self.board else "Draw"

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()
        
        if winner == self.ai_player:
            return 10 - depth
        elif winner == self.current_player:
            return depth - 10
        elif winner == "Draw":
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = self.ai_player
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = self.current_player
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = None
                        best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = float('-inf')
        move = (-1, -1)
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = self.ai_player
                    score = self.minimax(self.board.copy(), 0, False)
                    self.board[i][j] = None
                    if score > best_score:
                        best_score = score
                        move = (i, j)

        return move

    def play_game(self):
        while True:
            # Player's turn
            self.print_board()
            row = int(input("Enter your move row (0-2): "))
            col = int(input("Enter your move column (0-2): "))
            
            if (row < 0 or row > 2) or (col < 0 or col > 2) or (self.board[row][col] is not None):
                print("Invalid move. Try again.")
                continue
            
            # Update board with player's move
            self.board[row][col] = self.current_player
            
            # Check for a winner after player's move
            winner = self.check_winner()
            if winner:
                break
            
            # AI's turn
            ai_row, ai_col = self.ai_move()
            if ai_row != -1 and ai_col != -1: 
                self.board[ai_row][ai_col] = self.ai_player
            
            # Check for a winner after AI's move
            winner = self.check_winner()
            if winner:
                break
        
        # Final board state and result announcement
        self.print_board()
        print(f"Game Over! Winner: {winner}")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
