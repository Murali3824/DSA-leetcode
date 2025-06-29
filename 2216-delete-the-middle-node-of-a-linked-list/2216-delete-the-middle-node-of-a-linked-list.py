# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        middle = count // 2
        temp = head
        count = 0
        if middle == 0:
            head = head.next
            return
        while temp and count < middle-1:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next
        temp = head
        return temp
        