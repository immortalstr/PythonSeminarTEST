def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).rjust(4), end =' ')
        print()
print(print_operation_table(lambda x, y: x**y, 4, 4))
