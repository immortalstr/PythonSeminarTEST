def print_operation_table(operation, num_rows=6, num_columns=6):
    print("    ",end="")
    for i in range(1, num_rows + 1):
        print("{:4}".format(i),end=" ")
    print()
    print("     ",'-'* 4 * (num_columns + 1))
    for i in range(1, num_rows + 1):
        print(i,"|",end=" ")
        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).rjust(4), end =' ')
        print()
print_operation_table(lambda x, y: x**y, 6, 6)
