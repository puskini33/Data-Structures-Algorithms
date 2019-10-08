from Double_Linked_List import *
"""
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat
        swapped = false
        for i = 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap( A[i-1], A[i] )
                swapped = true
            end if
        end for
    until not swapped
end procedure


function merge_sort(list m)  # def merge_sort(list):
    if length of m =< 1 then  # if len(list) <= 1:
        return m                # return m

    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    left := merge_sort(left)
    right := merge_sort(right)

    return merge(left, right)

function merge(left, right)
    var result := empty list

    while left is not empty and right is not empty do
        if first(left) =< first(right) then
            append first (left) to result
            left := rest(left)
        else
            append first(right) to result
            right := rest(right)

    while left is not empty do
        append first(left) to result
        left := rest(left)
    while right is not empty do
        append first(right) to result
        right := rest(right)
    return result
"""


def bubble_sort(numbers):
    """Sort a list of numbers using bubble sort."""
    while True:
        is_sorted = True
        node = numbers.begin.next
        while node:
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                is_sorted = False
            node = node.next

        if is_sorted:
            break


"""def merge(left, right):
    result = []

    while left is not None and right is not None:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1, ]
        else:
            result.append(right[0])
            right = right[1, ]

    while left is not None:
        result.append(left[0])
        left = left[1, ]
    while right is not None:
        result.append(right[0])
        right = right[1, ]"""


def count_nodes(node: "DoubleLinkedListNode") -> int:
    """Counts the number of nodes in a list starting from the beginning node and returns the number of nodes."""
    count = 0
    while node:
        node = node.next
        count += 1

    return count


def merge_sort(numbers: 'DoubleLinkedList'):
    """Identifies the first node in the list and calls the merge_node function with the first node."""
    numbers.begin = merge_node(numbers.begin)


def merge_node(node: 'DoubleLinkedListNode') -> 'DoubleLinkedListNode':
    """Divides the list of nodes and finds the smallest unit in the list: the left node and the right node."""
    counted = count_nodes(node)  # the number of nodes in the list
    beginning_node = node
    if counted <= 1:
        return node
    else:
        mid_index = counted / 2
    for i in range(0, int(mid_index) - 1):
        node = node.next  # get the last node of the first half of the list

    begin_node_right = node.next
    node_end_left = node
    node_end_left.next = None
    begin_node_right.prev = None

    merged_left = merge_node(beginning_node)
    merged_right = merge_node(begin_node_right)

    return merge(merged_left, merged_right)


def merge(left: 'DoubleLinkedListNode', right: 'DoubleLinkedListNode') -> 'DoubleLinkedListNode':
    """Compares the left and right nodes and sorts them according to size."""
    result = None

    if left is None:
        return right
    if right is None:
        return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result


def get_node_at_index(list_node: 'DoubleLinkedList', index: int) -> 'DoubleLinkedListNode':
    """Returns node given specific index in the list."""
    node = list_node.begin
    count = 0
    while node and count < index:
        node = node.next
        count += 1

    return node


def quick_sort(numbers: 'DoubleLinkedList', lo: 'int', hi: 'int'):
    """Selects the area in the list to check for the size of nodes."""
    if lo < hi:
        p = partition(numbers, lo, hi)
        quick_sort(numbers, lo, p - 1)  # why is there here no error for when p is 0
        quick_sort(numbers, p + 1, hi)


def partition(numbers: 'DoubleLinkedList', lo: int, hi: int) -> int:
    """Selects a pivot, then places all numbers smaller than the pivot in the left side and all number bigger in the
    right side of the pivot."""
    pivot = get_node_at_index(numbers, hi)
    i = lo - 1

    for j in range(lo, hi):
        node_at_j = get_node_at_index(numbers, j)
        if node_at_j.value < pivot.value:
            i += 1
            if i != j:
                node_at_i = get_node_at_index(numbers, i)
                node_at_i.value, node_at_j.value = node_at_j.value, node_at_i.value  # swap the values of the nodes

    node_at_hi = get_node_at_index(numbers, hi)
    node_at_i = get_node_at_index(numbers, i + 1)

    if node_at_hi.value < node_at_i.value:
        node_at_hi.value, node_at_i.value = node_at_i.value, node_at_hi.value  # swap the position of the pivot

    return i + 1


"""
function insertSortR(array!, int n)
    if n > 0
        insertionSortR(A, n-1)
        x <- A[n]
        j <- n-1
        while j >= 0 and A[j] > x
            A[j+1] <- A[j]
            j <- j-1
        end while
        A[j+1] <- x
    end if
end function
"""


def insertSort(numbers, n: int):
    if n > 0:
        insertSort(numbers, n-1)
        if n == numbers.count():
            return
        node_at_n = get_node_at_index(numbers, n)
        j = n - 1
        node_at_j = get_node_at_index(numbers, j)
        while j >= 0 and node_at_j.value > node_at_n.value:
            node_at_bigger_j = get_node_at_index(numbers, j+1)
            node_at_j.value, node_at_bigger_j.value = node_at_bigger_j.value, node_at_j.value
            j = j-1
            node_at_j = get_node_at_index(numbers, j)
            node_at_bigger_j = get_node_at_index(numbers, j + 1)
            node_at_n = node_at_bigger_j
