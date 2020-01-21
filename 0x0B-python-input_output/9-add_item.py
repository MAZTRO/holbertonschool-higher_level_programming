#!/usr/bin/python3
import sys, json
load_js_file = __import__('8-load_from_json_file').load_from_json_file
save_js_file = __import__('7-save_to_json_file').save_to_json_file

try:
    my_list = []
    my_list = load_js_file("add_item.json")
    count = 0
    for av in sys.argv:
        if (count >= 1):
            my_list.append(av)
        count += 1
except FileNotFoundError:
    pass
finally:
        save_js_file(my_list, "add_item.json")

