# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left: List[ListNode], right: List[ListNode]) -> List[ListNode]:
        dummy = ListNode()
        temp = dummy
        if not left:
            return right
        elif not right:
            return left
        while left and right: 
            if left.val < right.val:
                temp.next = left       
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
            if left:
                temp.next = left
            if right:
                temp.next = right
        return dummy.next
 

    def mergeKLists(self, lists: List[Optional[ListNode]]):
        if not lists:  # Handle empty list case
            return None
        # Merge lists one by one
        merged_head = lists[0]
        for head in lists[1:]:
            merged_head = self.merge(merged_head, head)

        return merged_head


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        
        init = [(lists[i].val, i) for i in range(n) if lists[i]]
        if not init:
            return None
        heapq.heapify(init)
        result = ListNode()
        head = result
        while init:
            value, index = heapq.heappop(init)
            #index is the index of listnode
            head.next = lists[index]
            head = head.next
            lists[index] = lists[index].next
            #may be we push something
            if not lists[index]:
                continue
            newValue = lists[index].val
            if newValue < value:
                #add this value to result and continue
                head.next = lists[index]
                lists[index] = lists[index].next
                head = head.next
                continue
            heapq.heappush(init, (newValue,index))
            
        return result.next
