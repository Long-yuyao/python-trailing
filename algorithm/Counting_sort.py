"""
O(n)
make use of linear mapping
only for integer
"""


def distribution_counting_sort(l):
    maxl = max(l)
    minl = min(l)
    lconut = [0] * (maxl - minl + 1)
    lsorted = []
    for i in l:
        lconut[i - minl] = lconut[i - minl] + 1
    for i in range(len(lconut)):
        lsorted.extend([minl + i] * lconut[i])
    return lsorted


if __name__ == '__main__':
    assert distribution_counting_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert distribution_counting_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert distribution_counting_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
