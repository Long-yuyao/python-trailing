class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    """
    get min in constant time
    using assistant stack
    """

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


def min_stack_test():
    a = MinStack()
    a.push(0)
    a.push(-9)
    a.push(10)
    a.push(20)
    assert a.getMin() == -9


if __name__ == '__main__':
    min_stack_test()
