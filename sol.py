##problem1

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for num in nums:
            heapq.heappush((min_heap), num)

            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]
        

##problem2

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        myheap = []

        for i, k in enumerate(lists):
            if k:
                heapq.heappush(myheap,(k.val,i,k))
        
        while myheap:
            newval,i,newnode = heapq.heappop(myheap)
            curr.next = newnode
            curr = newnode 

            if newnode.next:
                heapq.heappush(myheap, (newnode.next.val,i,newnode.next))

        return dummy.next