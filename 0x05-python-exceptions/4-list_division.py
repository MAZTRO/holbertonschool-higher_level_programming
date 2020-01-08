#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(0, list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except IndexError:
            new_list.append(0)
            idx += 1
            print("out of range")
        except ZeroDivisionError:
            new_list.append(0)
            idx += 1
            print("division by 0")
        except TypeError:
            new_list.append(0)
            idx += 1
            print("wrong type")
        finally:
            pass
    return (new_list)
