"""
input：target = [9,3,5]
output：true
explanation：start from [1, 1, 1]
[1, 1, 1], sum is 3 ，location is 1
[1, 3, 1], sum is 5， location is 2
[1, 3, 5], sum is 9， location is 0
[9, 3, 5] successful
"""


def ispossible(target: list) -> bool:
    m = max(target)
    m_l = target.index(m)
    s = sum(target) - m
    if m > s and m != 1:
        if s == 1:
            target[m_l] = 1
        elif s == 0:
            if len(target) == 1 and target[0] == 1:
                return True
            else:
                return False
        else:
            target[m_l] = m % s
        return ispossible(target)
    elif m == 1 and 0 not in target:
        return True
    else:
        return False


if __name__ == '__main__':
    assert ispossible([9, 3, 5])
    assert ispossible([8, 5])
    assert ispossible([1, 1000000000]) is True
    assert ispossible([9, 9, 9]) is False
    assert ispossible([2, 900000002]) is False
    assert ispossible([2]) is False
