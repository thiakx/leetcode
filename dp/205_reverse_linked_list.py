class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


    # def reverseList(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     solution = Solution()
    #     prev = solution.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return prev