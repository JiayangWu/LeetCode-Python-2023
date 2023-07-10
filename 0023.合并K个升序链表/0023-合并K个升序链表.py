# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, i))
                lists[i] = lists[i].next

        dummy = ListNode(-1)
        p = dummy
        while min_heap:
            val, i = heappop(min_heap)
            p.next = ListNode(val, lists[i])
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
            
            p = p.next
        return dummy.next
