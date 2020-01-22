#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='utf-8') as my_file:
        empty_str = ""
        for line in my_file.readlines():
            if search_string in line:
                empty_str += line + new_string
            else:
                empty_str += line
    my_file.close()

    with open(filename, 'w') as my_file:
        my_file.write(empty_str)
    my_file.close()
