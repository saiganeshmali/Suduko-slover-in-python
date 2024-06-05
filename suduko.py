# def is_valid(board, row, col, num):
#     """Check if it's valid to place num at board[row][col]."""
#     for x in range(9):
#         if board[row][x] == num or board[x][col] == num or board[row - row % 3 + x // 3][col - col % 3 + x % 3] == num:
#             return False
#     return True

# def find_empty_location(board):
#     """Find an empty location in the board. Return (row, col) tuple or None if no empty cell."""
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return (i, j)
#     return None

# def solve_sudoku(board):
#     """Solve the Sudoku puzzle using backtracking."""
#     empty_location = find_empty_location(board)
#     if not empty_location:
#         return True  # Puzzle solved

#     row, col = empty_location

#     for num in range(1, 10):
#         if is_valid(board, row, col, num):
#             board[row][col] = num

#             if solve_sudoku(board):
#                 return True

#             # Reset the cell (backtrack)
#             board[row][col] = 0

#     return False

# # Example usage:
# sudoku_board = [
#     [0, 0, 0, 5, 4, 0, 0, 7, 8],
#     [0, 0, 6, 0, 0, 0, 0, 3, 0],
#     [0, 9, 8, 0, 0, 3, 0, 0, 0],
#     [0, 0, 7, 4, 0, 5, 0, 0, 3],
#     [0, 1, 0, 0, 3, 0, 7, 0, 5],
#     [4, 0, 0, 9, 7, 0, 8, 6, 0],
#     [0, 0, 0, 0, 9, 6, 0, 8, 0],
#     [0, 6, 9, 1, 0, 7, 3, 0, 4],
#     [1, 0, 3, 0, 0, 0, 9, 2, 0]
# ]

# if solve_sudoku(sudoku_board):
#     for row in sudoku_board:
#         print(row)
# else:
#     print("No solution exists.")



#  The player can input the Sudoku puzzle



def is_valid(board, row, col, num):
    """Check if it's valid to place num at board[row][col]."""
    for x in range(9):
        if board[row][x] == num or board[x][col] == num or board[row - row % 3 + x // 3][col - col % 3 + x % 3] == num:
            return False
    return True

def find_empty_location(board):
    """Find an empty location in the board. Return (row, col) tuple or None if no empty cell."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # Reset the cell (backtrack)
            board[row][col] = 0

    return False

def print_sudoku(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def read_sudoku_input():
    """Read Sudoku board from user input."""
    board = []
    print("Enter the Sudoku puzzle row by row, with 0 for empty cells. Separate numbers with spaces:")
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ").strip().split()
            if len(row) != 9:
                print("Each row must have 9 numbers. Please try again.")
                continue
            try:
                row = list(map(int, row))
                if any(num < 0 or num > 9 for num in row):
                    print("Numbers must be between 0 and 9. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            board.append(row)
            break
    return board

# Main function to run the Sudoku solver with player input
def main():
    sudoku_board = read_sudoku_input()
    print("\nInput Sudoku board:")
    print_sudoku(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku board:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists.")

if __name__ == "__main__":
    main()
