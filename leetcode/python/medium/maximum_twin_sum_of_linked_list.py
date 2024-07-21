# task number - 2130


class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node


def max_twin_pair_sum(head: ListNode or None) -> int:
    if not head:
        return 0

    # detect middle node

    slow_node = head
    fast_node = head

    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

    middle_node = slow_node

    # reverse second half of linked list

    prev_node = None
    current_node = middle_node

    while current_node:
        current_next = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = current_next

    reverse_head = prev_node

    # iterate over both parts and select max pair sum

    max_twin_sum = 0

    while head and reverse_head:
        max_twin_sum = max(max_twin_sum, head.val + reverse_head.val)
        head = head.next
        reverse_head = reverse_head.next

    return max_twin_sum


if __name__ == '__main__':
    input_head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    print(f'Maximum twin pair sum for the input head - {max_twin_pair_sum(input_head)}')  # 6

    input_head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    print(f'Maximum twin pair sum for the input head - {max_twin_pair_sum(input_head)}')  # 7

    input_head = ListNode(1, ListNode(100))
    print(f'Maximum twin pair sum for the input head - {max_twin_pair_sum(input_head)}')  # 101
