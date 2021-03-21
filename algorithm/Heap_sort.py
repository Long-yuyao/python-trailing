"""
O(nlog(n))
create heap
do del max key while heap
"""
import data_structure.heap.heap_basic


def heap_sort(heap):
    h = data_structure.heap.heap_basic.Heap(heap).create_bottom_up()
    hed = []
    while h:
        hed.append(h[0])
        h.pop(0)
        h = data_structure.heap.heap_basic.Heap(h).create_bottom_up()
    hed.reverse()
    return hed


if __name__ == '__main__':
    assert heap_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert heap_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert heap_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
    assert heap_sort(['a', 'b', 'c']) == ['a', 'b', 'c']
