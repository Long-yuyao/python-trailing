class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2
