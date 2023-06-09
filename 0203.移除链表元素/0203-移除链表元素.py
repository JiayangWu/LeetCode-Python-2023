# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        p = dummy
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy.next