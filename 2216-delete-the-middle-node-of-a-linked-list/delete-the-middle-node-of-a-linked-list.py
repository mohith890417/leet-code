# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if there is only one node, deleting it leaves an empty list
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Delete the middle node
        prev.next = slow.next
        
        return head