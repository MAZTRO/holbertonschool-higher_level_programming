#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(-10)
my_list.append("a")
my_list.append(576)
my_list.append(6.9)
my_list.append(True)
my_list.append((3, 4, 6))
print(my_list)
my_list.print_sorted()
