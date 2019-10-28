# This is an implementation of the binary search for the python list.


def _find_number(x, m, manual_list):
    if x == manual_list[m]:
        return x
    elif x > manual_list[m]:  # if the number is bigger than value at index m
        new_list = manual_list[m+1:]
        m = len(new_list) // 2
        _find_number(x, m, new_list)
    elif x < manual_list[m]:  # if the number is smaller than value at index m
        new_list = manual_list[:m-1]
        m = len(new_list) // 2
        _find_number(x, m, new_list)

    return x


def find_number(x, manual_list):
    m = len(manual_list) // 2
    found = _find_number(x, m, manual_list)
    return found
