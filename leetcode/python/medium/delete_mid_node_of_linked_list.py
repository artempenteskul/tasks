# task number - 2095


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def delete_middle_node(head: ListNode) -> ListNode or None:
    if not head.next:
        return None

    prev_node = None
    slow_node = head
    fast_node = head

    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        prev_node = slow_node
        slow_node = slow_node.next

    prev_node.next = slow_node.next

    return head


if __name__ == '__main__':
    input_head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    output_head = delete_middle_node(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head values for input head: {output_list}')  # [1, 3, 4, 1, 2, 6]

    ###

    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    output_head = delete_middle_node(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head values for input head: {output_list}')  # [1, 2, 4]

    ###

    input_head = ListNode(2, ListNode(1))
    output_head = delete_middle_node(input_head)

    output_list = []
    while output_head:
        output_list.append(output_head.val)
        output_head = output_head.next

    print(f'Output head values for input head: {output_list}')  # [2]
