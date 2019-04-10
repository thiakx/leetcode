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

    # #recursion
    #  def reverseList(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     else:
    #         solution = Solution()
    #         prev = solution.reverseList(head.next)
    #         # let n_(k+1) point back to n_k
    #         head.next.next = head
    #         # drop the original pointer so wont have loop
    #         head.next = None
    #         return prev