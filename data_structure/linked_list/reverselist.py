# https://leetcode-cn.com/problems/reverse-linked-list/
# class Node:
#     def __init__(self, value: int):
#         self.value = value
#         self.next = None
#
#
# def reverse_list(start: Node) -> Node:
#     end = None
#     while start:
#         p = Node(start.value)
#         p.next = end
#         end = p
#         start = start.next
#     return end
#
#
# if __name__ == '__main__':
#     rl = Node(1)
#     rl.next = Node(3)
#     rl.next.next = Node(8)
#     rl.next.next.next = Node(9)
#     rl.next.next.next.next = Node(0)
#     l = reverse_list(rl)
#     while l:
#         print(l.value)
#         l = l.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rl = None
        tmp = head
        while tmp:
            newpoint = ListNode(tmp.val)
            newpoint.next = rl
            rl = newpoint
            tmp = tmp.next
        return rl


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
head = Solution().reverseList(a)
while head:
    print(head.val)
    head = head.next
