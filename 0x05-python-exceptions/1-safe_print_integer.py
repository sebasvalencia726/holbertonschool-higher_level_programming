#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value and not isinstance(value, bool):
            print("{:d}".format(value))
            return True
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False
