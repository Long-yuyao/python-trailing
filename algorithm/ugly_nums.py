"""
https://leetcode-cn.com/problems/chou-shu-lcof
"""
def nthUglyNumber(n: int) -> int:
    count = 5
    waiting = [1, 2, 3, 4, 5]
    done = [[2, 1], [3, 1], [5, 3]]
    if n <= 5:
        return waiting[n-1]
    else:
        while count < n:
            x = done[0][0] * (waiting[done[0][1] + 1])
            y = done[1][0] * (waiting[done[1][1] + 1])
            z = done[2][0] * (waiting[done[2][1] + 1])
            m = min(x, y, z)
            if m == x:
                done[0][1] = done[0][1] + 1
            if m == y:
                done[1][1] = done[1][1] + 1
            if m == z:
                done[2][1] = done[2][1] + 1
            waiting.append(m)
            count = count + 1
        print(waiting)
        return waiting[count - 1]


if __name__ == '__main__':
    assert nthUglyNumber(10) == 12
