# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list = []
        
        i = 0
        while len(list1) > 0 or len(list2) > 0:
            if len(list1) > 0:
                if len(list2) > 0:
                    if list1[i] > list2[i]:
                        final_list.append(list2.pop())
                    else:
                        final_list.append(list1.pop())
                else:
                    final_list.append(list1.pop())

            i += 1

        return final_list

if __name__ == '__main__':
    s = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]

    assert s.mergeTwoLists(list1, list2) == [1,1,2,3,4,4]

    list1 = []
    list2 = []

    assert s.mergeTwoLists(list1, list2) == []

    list1 = []
    list2 = [0]

    assert s.mergeTwoLists(list1, list2) == [0]