# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        fast, slow, prev_node = head, head, None

        while not fast == None and not fast.next == None:
            prev_node = slow
            slow = slow.next
            fast = fast.next.next
        if prev_node:
            prev_node.next = None
        else:
            head = None
        # reverse the second half
        prev = None
        mid = slow

        while mid:
            next_temp = mid.next
            mid.next = prev
            prev = mid
            mid = next_temp

        dummy = ListNode()
        tail = dummy
        # add from each
        while not prev == None:
            if head:
                tail.next = head
                head = head.next
                tail = tail.next
            tail.next = prev
            prev = prev.next
            tail = tail.next
        return None
            