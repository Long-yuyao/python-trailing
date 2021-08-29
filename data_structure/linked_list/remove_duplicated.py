# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        vertex = head
        while vertex.next:
            if vertex.next.val == vertex.val:
                    vertex.next = vertex.next.next
            else:
                vertex = vertex.next
        return head


a = ListNode(2)
b = ListNode(2)
c = ListNode(2)
d = ListNode(5)
a.next = b
b.next = c
c.next = d
head = Solution().deleteDuplicates(a)
while head:
    print(head.val)
    head = head.next