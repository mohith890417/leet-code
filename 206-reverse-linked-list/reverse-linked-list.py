# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # Temporarily store the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move the prev pointer forward
            curr = next_temp       # Move the curr pointer forward
            
        return prev                # prev will be the new head of the reversed list