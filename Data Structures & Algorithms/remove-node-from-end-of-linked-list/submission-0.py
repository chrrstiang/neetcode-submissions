# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        prev_node = slow

        for i in range(n):
            fast = fast.next
        
        while not fast == None:
            prev_node = slow
            slow = slow.next
            fast = fast.next
        
        prev_node.next = slow.next

        return dummy.next