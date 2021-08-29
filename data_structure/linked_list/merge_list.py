# https://leetcode-cn.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        firsthead = ListNode(-10000)
        mp = firsthead
        while l1 and l2:
            if l1.val <= l2.val:
                mp.next = l1
                mp = mp.next
                l1 = l1.next
            else:
                mp.next = l2
                mp = mp.next
                l2 = l2.next
        if not l1:
            mp.next = l2
        else:
            mp.next = l1
        return firsthead.next
