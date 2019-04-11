# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# from forums
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = head
        fast = head
        # fast will go 2x as fast, completing the loop when slow reach mid point & reversing
        while fast and fast.next:
            fast = fast.next.next
            # expressions on the right side are evaluated before any of the assignments,
            # and then they are assigned one by one, from left to right.
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
