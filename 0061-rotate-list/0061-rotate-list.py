# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        #Compute The length
        curr = head
        length = 0
        last = None
        while curr:
            last = curr
            curr = curr.next
            length+=1

        last.next = head #Make the list Circular

        #Find the Tail
        k = length - (k%length)
        while k:
            last = last.next
            k-=1

        #Break the circle and return the New Head
        newHead = last.next
        last.next = None
        return newHead