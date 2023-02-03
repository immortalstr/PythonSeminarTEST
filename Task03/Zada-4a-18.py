my_list = [int(input('type element: ')) for i in range(int(input('type amount: ')))]
x = int(input('type X: '))
min_list = my_list[0]
for i in range(len(my_list)):
    if  my_list[i] <= x and my_list[i] > min_list:
        min_list = my_list[i]
        if  (my_list[i] >= x and my_list[i] <= x) and my_list[i] > min_list:
            min_list = my_list[i]

print(min_list)