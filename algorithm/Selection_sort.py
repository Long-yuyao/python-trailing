"""
O(n^2)
assume min
compare element in list with min
"""


def selection_sort(matrix):
    for i in range(len(matrix) - 1):
        min_obj = i
        for j in range(len(matrix) - i):
            if matrix[i + j] < matrix[min_obj]:
                min_obj = i + j
        c = matrix[min_obj]
        matrix[min_obj] = matrix[i]
        matrix[i] = c
    return matrix


if __name__ == '__main__':
    assert selection_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert selection_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert selection_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
    assert selection_sort(['a', 'b', 'c']) == ['a', 'b', 'c']
