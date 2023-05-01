# task number - 21


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head_node = dummy_node = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            dummy_node.next = list1
            list1 = list1.next
        else:
            dummy_node.next = list2
            list2 = list2.next

        dummy_node = dummy_node.next

    if list1:
        dummy_node.next = list1

    if list2:
        dummy_node.next = list2

    return head_node.next


if __name__ == '__main__':
    l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    res = merge_two_sorted_lists(l1, l2)  # [1, 1, 2, 3, 3, 4]

    res_list = []
    while res:
        res_list.append(res.val)
        res = res.next

    print(res_list)


# def merge_two_sorted_lists_2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     head_node = None
#     temp_node = ListNode()
#
#     while list1 or list2:
#         if not list1:
#             current_value = list2.val
#             list2 = list2.next
#         elif not list2:
#             current_value = list1.val
#             list1 = list1.next
#         else:
#             if list1.val <= list2.val:
#                 current_value = list1.val
#                 list1 = list1.next
#             else:
#                 current_value = list2.val
#                 list2 = list2.next
#
#         if head_node is None:
#             head_node = ListNode(current_value, temp_node)
#         else:
#             temp_node.val = current_value
#             if list1 or list2:
#                 temp_node.next = ListNode()
#                 temp_node = temp_node.next
#
#     return head_node
