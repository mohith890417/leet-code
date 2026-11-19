# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast ahead by n + 1 steps so slow stops right before the target node
        for _ in range(n + 1):
            fast = fast.next

        # Advance both pointers until fast hits the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Unlink the nth node from the end
        slow.next = slow.next.next
        return dummy.next