# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        prefix_sum2Node = dict()
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum2Node[0] = dummy
        p = dummy
        while p:
            prefix_sum += p.val
            prefix_sum2Node[prefix_sum] = p
            p = p.next
        p = dummy
        prefix_sum = 0
        while p:
            prefix_sum += p.val
            if prefix_sum in prefix_sum2Node:
                p.next = prefix_sum2Node[prefix_sum].next
            p = p.next
        return dummy.next