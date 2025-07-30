# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        min_heap = []

        # Push all values from all lists into the min heap
        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next

        dummy = ListNode(0)
        current = dummy

        # Build the sorted list from heap
        while min_heap:
            current.next = ListNode(heapq.heappop(min_heap))
            current = current.next

        return dummy.next
        