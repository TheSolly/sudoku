# [http://en.wikipedia.org/wiki/Sudoku]

# A procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

incorrect6 = [[2, 2, 2],
              [2, 2, 2],
              [2, 2, 2]]


def check_sudoku(p):
    n = len(p)  # Extract size of grid
    digit = 1  # start with 1
    while digit <= n:  # go Through each digit
        i = 0
        while i < n:  # Go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n:  # for each entry in it row/column
                if p[i][j] == digit:  # check row count
                    row_count = row_count + 1
                if p[j][i] == digit:  # check column count
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1  # next row/column
        digit = digit + 1  # next digit
    return True  # nothing was wrong


print check_sudoku(incorrect)
# >>> False

print check_sudoku(correct)
# >>> True

print check_sudoku(incorrect2)
# >>> False

print check_sudoku(incorrect3)
# >>> False

print check_sudoku(incorrect4)
# >>> False

print check_sudoku(incorrect5)
# >>> False

print check_sudoku(incorrect6)
# >>> False
