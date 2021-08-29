# https://leetcode-cn.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        fast = head.next.next
        slow = head.next
        flag = False
        while slow and fast and fast.next:
            if slow == fast:
                flag = True
                break
            slow = slow.next
            fast = fast.next.next
        fast = head
        if flag:
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        return


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c
print(Solution().detectCycle(a).val)
