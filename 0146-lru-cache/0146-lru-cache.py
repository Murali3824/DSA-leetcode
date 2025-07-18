class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key to node

        # Dummy nodes for head (left) and tail (right)
        self.head = Node(0, 0)  # Most recent
        self.tail = Node(0, 0)  # Least recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_left(self, node):
        """Add new node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Remove node from list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_left(self, node):
        """Move accessed node to the left (MRU)."""
        self._remove(node)
        self._add_left(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_left(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to front
            node = self.cache[key]
            node.value = value
            self._move_to_left(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove LRU (from right)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            # Add new node to left
            new_node = Node(key, value)
            self._add_left(new_node)
            self.cache[key] = new_node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)