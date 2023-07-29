# Write a function that takes in an nxm two-dimensional array and returns all the elements in spiral order
# ex:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# would return: [1, 2, 3, 4, 5, 6, 7, 8, 9]

def spiral(array):
    start_col = 0
    start_row = 0
    end_col = len(array[0]) - 1
    end_row = len(array) - 1
    output = []
    while start_col <= end_col and start_row <= end_row:
        for col in range(start_col, end_col + 1):
            output.append(array[start_row][col])
        start_row += 1

        if start_row > end_row:
            break

        for row in range(start_row, end_row + 1):
            output.append(array[row][end_col])
        end_col -= 1

        if start_col > end_col:
            break

        for col in reversed(range(start_col, end_col + 1)):
            output.append(array[end_row][col])
        end_row -= 1

        for row in reversed(range(start_row, end_row + 1)):
            output.append(array[row][start_col])
        start_col += 1
            
    return output


if __name__ == "__main__":
    array =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    spiral(array)