"""
O(n^2)
a,b,c (ascent)
if a>b, change (a,b)
"""


class BubbleSort:
    def bubble_sort(self, matrix) -> list:
        for i in range(len(matrix) - 1):
            for j in range(1, len(matrix)-i):
                if matrix[i] > matrix[i+j]:
                    c = matrix[i+j]
                    matrix[i+j] = matrix[i]
                    matrix[i] = c
        return matrix


if __name__ == '__main__':
    assert BubbleSort().bubble_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert BubbleSort().bubble_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert BubbleSort().bubble_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
    assert BubbleSort().bubble_sort(['a', 'b', 'c']) == ['a', 'b', 'c']

