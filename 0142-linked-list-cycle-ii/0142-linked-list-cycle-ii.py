class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected
                entry = head
                index = 0
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                    index += 1
                print("tail connects to the index", index)
                return entry  # ✅ Must return here to avoid infinite loop

        print("no cycle")
        return None
