"""
Giving a set of coins, and their value are c1,c2...cn
How to choose coins to achieve that the summary of selected coins is the largest where any location of coins are
not adjoining?

F(n)=max(cn+F(n-2),F(n-1))
"""

"""
there are n oranges,you have three choices to eat them:
1. eat 1
2. if n%2 == 0, eat n/2
3. if n%3 == 0, eat 2n/3
return the least day
"""


def min_days(n: int) -> int:
    if n < 3:
        return n
    else:
        return min(n % 2 + 1 + min_days(int(n/2)), n % 3 + 1 + min_days(int(n/3)))


if __name__ == '__main__':
    assert min_days(10) == 4
    assert min_days(6) == 3
    assert min_days(1) == 1
    assert min_days(56) == 6
