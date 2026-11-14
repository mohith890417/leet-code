import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.min_heap = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.in_heap.remove(smallest)
            return smallest
        
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.in_heap:
            heapq.heappush(self.min_heap, num)
            self.in_heap.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)