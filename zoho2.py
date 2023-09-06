def find_rectangle_and_sum(mat, start_index, end_index):
    row_start, col_start = start_index
    row_end, col_end = end_index
    rectangle = []
    rectangle_sum = 0
    for i in range(row_start, row_end + 1):
        row = []
        for j in range(col_start, col_end + 1):
            row.append(mat[i][j])
            rectangle_sum += mat[i][j]
        rectangle.append(row)
    return rectangle, rectangle_sum
mat = [[1, 2, 3, 4, 6], [5, 3, 8, 1, 2], [4, 6, 7, 5, 5], [2, 4, 8, 9, 4]]
start_index = (0, 0)
end_index = (3, 4)
rectangle, rectangle_sum = find_rectangle_and_sum(mat, start_index, end_index)
print("Rectangle:")
for row in rectangle:
    print(" ".join(map(str, row)))
print("Sum:", rectangle_sum)
