# task number - 2807


import math


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def insert_greatest_common_divisors(head: ListNode) -> ListNode:
    if not head.next:
        return head

    curr = head
    while curr.next:
        gdc_node = ListNode(math.gcd(curr.val, curr.next.val), next_node=curr.next)
        curr.next = gdc_node
        curr = curr.next.next

    return head


if __name__ == '__main__':
    input_head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    result_head = insert_greatest_common_divisors(input_head)
    result_list = []
    while result_head:
        result_list.append(result_head.val)
        result_head = result_head.next

    print(f'Result for input head - {result_list}')  # [18, 6, 6, 2, 10, 1, 3]

    ###

    input_head = ListNode(1)
    result_head = insert_greatest_common_divisors(input_head)
    result_list = []
    while result_head:
        result_list.append(result_head.val)
        result_head = result_head.next

    print(f'Result for input head - {result_list}')  # [1]
