# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome_o1space(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        reverse = None

        once = head
        twice = head

        while(twice != None and twice.next != None):
            temp = once
            once = once.next
            twice = twice.next

            if twice != None:
                twice = twice.next

            temp.next = reverse
            reverse = temp

        if twice != None:
            once = once.next

        while(once != None):
            if once.val != reverse.val:
                return False

            reverse = reverse.next
            once = once.next

        return True

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return True

    stack = []

    once = head
    twice = head
    while(twice != None and twice.next != None):
        stack.append(once.val)
        once = once.next

        twice = twice.next
        if twice != None:
            twice = twice.next


    if twice != None:
        once = once.next

    while(once != None):
        if once.val != stack.pop():
            return False
        once = once.next

    return True
