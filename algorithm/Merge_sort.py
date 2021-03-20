"""
O(nlogn)
A[0...n]->A1[0..n/2],A2[n/2+1...n](bubble/selection/insertion)
merge A1,A2
"""
import Insertion_sort


def merge_sort(a):
    a_asc = []
    m = int(len(a)/2)
    a1 = Insertion_sort.insertion_sort(a[:m])
    a2 = Insertion_sort.insertion_sort(a[m:])
    i = 0
    j = 0
    while i <= (m-1) and j <= len(a)-m-1:
        if a1[i] > a2[j]:
            a_asc.append(a2[j])
            j = j+1
        else:
            a_asc.append(a1[i])
            i = i+1
    if i > m-1:
        a_asc.extend(a2[j:])
    else:
        a_asc.extend(a1[i:])
    return a_asc


if __name__ == '__main__':
    assert merge_sort([4, 13, 5, 9, 10, 8]) == [4, 5, 8, 9, 10, 13]
    assert merge_sort([4, 13, 5, 9, 10, 5]) == [4, 5, 5, 9, 10, 13]
    assert merge_sort([4, 13, -1, 9, 10, 8]) == [-1, 4, 8, 9, 10, 13]
    assert merge_sort(['a', 'b', 'c']) == ['a', 'b', 'c']


