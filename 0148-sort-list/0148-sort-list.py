# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Step 2: Sort the list
        values.sort()

        # Step 3: Rebuild linked list
        dummy = ListNode()
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
        