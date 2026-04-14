#1. Reversed List
class Solution(object):
    def reverseList(self, head):
        prev_node = None
        curr_node = head

        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node
    
#2. Merging lists
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node = ListNode()
        sentinel = node

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return sentinel.next