# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            sum_var = carry
            if l1:
                sum_var += l1.val
                l1 = l1.next
            if l2:
                sum_var += l2.val
                l2 = l2.next
            carry  = sum_var // 10
            current.next = (ListNode(sum_var % 10))
            current = current.next
        return dummy.next

        