"""
if the summary of sub_list is more than k, then return the minimum length of sub_list, else return -1
time limited
"""


def shortestsubarray(A: list, K: int) -> int:
    ml = len(A)
    ans = ml
    B = [0]
    stack = [0]
    for i in A:
        B.append(B[-1] + i)
    for i in range(1, ml + 1):
        while stack and B[stack[-1]] >= B[i]:  # if B[i]>B[j] and j>i then we choose j as final
            stack.pop()
        stack.append(i)
        while stack and B[stack[-1]] - B[stack[0]] >= K:
            # after demind some larger than K, we can del it
            ans = min(ans, stack[-1] - stack[0])
            stack.pop(0)
    if B[ml] < K and ans == ml:
        return -1
    return ans


if __name__ == '__main__':
    assert shortestsubarray([2, -1, 2], 3) == 3
    assert shortestsubarray([1], 1) == 1
    assert shortestsubarray([1, 2], 4) == -1
    assert shortestsubarray([77, 19, 35, 10, -14], 5) == 1
    assert shortestsubarray([84, -37, 32, 40, 95], 167) == 3
    assert shortestsubarray([75, -32, 50, 32, 97], 129) == 2
    assert shortestsubarray([48, 99, 37, 4, -31], 140) == 2
