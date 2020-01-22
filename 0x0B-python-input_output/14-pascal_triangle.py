#!/usr/bin/python3
def pascal_triangle(n):
    if n == 1:
        return ([[1]])
    elif n <= 0:
        return ([])
    else:
        list_1 = []
        list_2 = []
        count_2 = 0

        list_1.append(1)
        list_2.append(list_1)
        for count in range(n - 1):
            list_1 = []
            tmp_list = list_2[-1]
            while count_2 < len(tmp_list):
                if count_2 != 0:
                    list_1.append(tmp_list[count_2] + tmp_list[count_2 - 1])
                else:
                    list_1.append(1)
                count_2 += 1
            list_1.append(1)
            list_2.append(list_1)
        return (list_2)
