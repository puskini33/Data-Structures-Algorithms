from DoubleLinkedList_v4 import *


def _bsearch_ll(value: int, given_list: 'DoubleLinkedList') -> int or None:
    """Function takes a DoubleLinkedList, finds the median, searches for a given value and returns the value or None."""
    m = given_list.count // 2
    m_value = given_list.get(m)
    if value == m_value:
        return value
    elif value != m_value and given_list.count == 1:  # if there is 1 node left, but it does not match value
        value = None
        return value
    elif value > m_value:
        new_list = DoubleLinkedList()
        number_nodes = given_list.count
        for i in range(m+1, number_nodes):  # range between m + 1 and the number of nodes creates DLL from the right side
            i_value = given_list.get(i)
            new_list.push(i_value)
        return _bsearch_ll(value, new_list)
    elif value < m_value:
        new_list = DoubleLinkedList()
        for j in range(0, m):  # range between m + 1 and the number of nodes creates DLL from the left side
            j_value = given_list.get(j)
            new_list.push(j_value)
        return _bsearch_ll(value, new_list)


def bsearch_ll(value: int or str, given_list: 'DoubleLinkedList') -> int or None:
    m = given_list.count // 2
    m_value = given_list.get(m)
    if value == m_value:
        return value
    else:
        found = _bsearch_ll(value, given_list)
        return found
