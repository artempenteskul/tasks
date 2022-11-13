from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        temp_node = ListNode()

        if list1.val <= list2.val:
            head_node = ListNode(list1.val, temp_node)
            list1 = list1.next
        else:
            head_node = ListNode(list2.val, temp_node)
            list2 = list2.next

        while list1 is not None or list2 is not None:
            if list1 is None:
                temp_node.val = list2.val
                list2 = list2.next
            elif list2 is None:
                temp_node.val = list1.val
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    temp_node.val = list1.val
                    list1 = list1.next
                else:
                    temp_node.val = list2.val
                    list2 = list2.next

            if list1 is not None or list2 is not None:
                temp_node.next = ListNode()
                temp_node = temp_node.next

        return head_node


if __name__ == '__main__':
    l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    res = Solution.merge_two_lists(l1, l2)

    res_list = []
    while res:
        res_list.append(res.val)
        res = res.next

    print(res_list)
