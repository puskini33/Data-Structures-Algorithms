# This is an implementation of the binary search for the python list.


def _find_number(x, m, manual_list):
    if x == manual_list[m]:
        return x
    elif x != manual_list[m] and len(manual_list) == 1:
        x = None
        return x
    elif x > manual_list[m]:  # if the number is bigger than value at index m
        new_list = manual_list[m+1:]
        if len(new_list) % 2 == 0:
            m = len(new_list) // 2 - 1
        else:
            m = len(new_list) // 2
        return _find_number(x, m, new_list)
    elif x < manual_list[m]:  # if the number is smaller than value at index m
        new_list = manual_list[:m]
        if len(new_list) % 2 == 0:
            m = len(new_list) // 2 - 1
        else:
            m = len(new_list) // 2
        return _find_number(x, m, new_list)


def find_number(x, man_list):
    if len(man_list) % 2 == 0:
        m = len(man_list) // 2
    else:
        m = len(man_list) // 2 + 1
    found = _find_number(x, m, man_list)
    return found
