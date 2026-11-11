# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # Step 3: Find the maximum twin sum by traversing both halves
        max_sum = 0
        first = head
        second = prev  # 'prev' is now the head of the reversed second half
        
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
            
        return max_sum