# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#快指针和慢指针
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = ListNode(-10000, head)
        slow = newhead
        while slow and slow.next:
            fast = slow.next
            while fast.next and fast.next.val == fast.val:
                fast = fast.next
            if fast != slow.next:
                slow.next = fast.next
            else:
                slow = slow.next
        return newhead.next


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
head = Solution().deleteDuplicates(a)
while head:
    print(head.val)
    head = head.next
