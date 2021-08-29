# https://leetcode-cn.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        while head:
            val.append(head.val)
            head = head.next

        return val == val[::-1]


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(2)
f = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(Solution().isPalindrome(a))