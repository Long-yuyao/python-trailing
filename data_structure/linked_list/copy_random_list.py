# https://leetcode-cn.com/problems/copy-list-with-random-pointer/
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited.keys():
            return self.visited[head]
        newnode = Node(head.val)
        self.visited[head] = newnode
        newnode.next = self.copyRandomList(head.next)
        newnode.random = self.copyRandomList(head.random)
        return newnode


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
a.random = c
b.next = a
b.random = None
c.next = b
c.random = a
print(Solution().copyRandomList(a).next.val)

