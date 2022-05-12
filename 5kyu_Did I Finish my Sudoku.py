''''
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:


There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

Columns:


There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

Regions


A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:


For those who don't know the game, here are some information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/

'''

def done_or_not(board): #board[i][j]

    def rows_done(board):
        for row in range(len(board)):
            row_set = []
            for n in range(len(board[row])):
                row_set.append(board[row][n])
            if len(set(row_set)) != 9:
                return False
        return True

    def columns_done(board):
        for row in range(len(board)):
            column_set = []
            for col in range(len(board[row])):
                column_set.append(board[col][row])
            if len(set(column_set)) != 9:
                return False

        return True

    def squares_done(board):
        for x1 in range(3):
            for y1 in range(3):
                square_set = []
                for x2 in range(3):
                    for y2 in range(3):
                        x = x1*3 + x2
                        y = y1*3 + y2
                        square_set.append(board[x][y])
                if len(set(square_set)) != 9:
                    return False
        return True
    
    if rows_done(board) and columns_done(board) and squares_done(board):
        return 'Finished!'
    return 'Try again!'

'''
BEST SOLUTION:

import numpy as np
def done_or_not(aboard): #board[i][j]
  board = np.array(aboard)

  rows = [board[i,:] for i in range(9)]
  cols = [board[:,j] for j in range(9)]
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  
  for view in np.vstack((rows,cols,sqrs)):
      if len(np.unique(view)) != 9:
          return 'Try again!'
  
  return 'Finished!'
'''