
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total, carry = 0, 0
        current_node, first_node = None, None
        while l1 or l2 or carry:
            curr_digit = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if curr_digit >= 10:
                carry = 1
                curr_digit -= 10
            else:
                carry = 0
            new_node = ListNode(curr_digit)
            if current_node:
                current_node.next = new_node
            else:
                first_node = new_node
            current_node = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return first_node


    