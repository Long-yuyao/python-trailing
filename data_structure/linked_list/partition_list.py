# https://leetcode-cn.com/problems/partition-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lfirstpoint = ListNode(-1000)
        lessp = lfirstpoint
        rfirstpoint = ListNode(-1000)
        morep = rfirstpoint
        while head:
            if head.val < x:
                lessp.next = head
                lessp = lessp.next
            else:
                morep.next = head
                morep = morep.next
            head = head.next
        morep.next = None
        lessp.next = rfirstpoint.next
        return lfirstpoint.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head = Solution().partition(a, 3)
while head:
    print(head.val)
    head = head.next
