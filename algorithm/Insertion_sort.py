"""
O(n^2)
1,4,2,7,13
1
1,4
1,2,4
1,2,4,7
1,2,4,7,13
"""


def insertion_sort(matrix):
    for i in range(len(matrix) - 1):
        v = matrix[i+1]
        j = i
        while v < matrix[j] and j >= 0:
            matrix[j+1] = matrix[j]
            j = j - 1
        matrix[j+1] = v
    return matrix


if __name__ == '__main__':
    assert insertion_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert insertion_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert insertion_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
    assert insertion_sort(['a', 'b', 'c']) == ['a', 'b', 'c']
