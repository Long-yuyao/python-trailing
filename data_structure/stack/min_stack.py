import math


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        m = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append([val, m])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def min_stack_test():
    a = MinStack()
    a.push(None)
    a.push(0)
    a.push(1)
    print(a.getMin())
    a.pop()
    print(a.getMin())


if __name__ == '__main__':
    min_stack_test()
