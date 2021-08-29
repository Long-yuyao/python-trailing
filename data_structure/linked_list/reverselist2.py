# https://leetcode-cn.com/problems/reverse-linked-list-ii/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        headfirst = ListNode(-1000)
        prl = headfirst
        count = 1
        while count < left and head:
            prl.next = head
            head = head.next
            prl = prl.next
            count = count + 1
        rl = None
        while count <= right and head:
            newpoint = ListNode(head.val)
            newpoint.next = rl
            if count == left:
                endpl = newpoint
            rl = newpoint
            head = head.next
            count = count + 1
        endpl.next = head
        prl.next = rl
        return headfirst.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
head = Solution().reverseBetween(a, 2, 6)
while head:
    print(head.val)
    head = head.next
