#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for fold in dir(hidden_4):
        if fold[0] != '_' and fold[1] != '_':
            print("{}".format(fold))
