# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if odd == None:
            return None

        even = head.next
        if even == None:
            return head

        first_even = even

        while(True):
            # keep track of current odd node and get next odd node if exist
            last_odd = odd
            odd = odd.next
            if odd:
                odd = odd.next

            # keep track of current even node and get next even node if exist
            last_even = even
            even = even.next
            if even:
                even = even.next

            last_even.next = even
            last_odd.next = odd

            if odd and not even:
                odd.next = first_even
                return head
            elif not odd:
                last_odd.next = first_even
                return head
