"""
Remove Islands - Medium

Write a function that accepts a two-dimensonal array containing 0's and 1's.
An island is defined as any number of 1's that are horizontally or vertically adjacent and are not touching the borders of the arrays.
Return the two-dimensional array with all the valid islands removed.


Optimal time complexity: O(w * h)
Optimal space complexity: O(w * h)

*****
* h: height of the two dimensional array (num rows)
* w: width (length of longest array)
"""

def remove_islands(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    # check borders
    for row in range(n_rows):
        for col in range(n_cols):
            if (row > 0 and row < n_rows - 1) and (col > 0 and col < n_cols - 1):
                continue
            traverse(matrix, row, col, True)
    # travserse interior    
    for row in range(n_rows):
        for col in range(n_cols):
            traverse(matrix, row, col, False)

    # change 2's back to 1's
    for row in range(n_rows):
        for col in range(n_cols):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
    
    return matrix


def traverse(matrix, row, col, is_border):
    if matrix[row][col] != 1:
        return
    if is_border:
        matrix[row][col] = 2
    else:
        matrix[row][col] = 0

    if row > 0:
        traverse(matrix, row-1, col, is_border)
    if col > 0:
        traverse(matrix, row, col-1, is_border)
    if row < len(matrix) - 1:
        traverse(matrix, row+1, col, is_border)
    if col < len(matrix[0]) - 1:
        traverse(matrix, row, col+1, is_border)




if __name__ == "__main__":
    matrix = [

    ]
    remove_islands(matrix)