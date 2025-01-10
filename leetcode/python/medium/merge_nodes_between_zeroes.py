# task number - 2181
# topics - linked list, simulation


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node


def merge_nodes(head: ListNode) -> ListNode:
    new_head = head

    while head.next:
        head.val += head.next.val

        if head.next.val == 0 and head.val != 0:
            if head.next.next:
                head = head.next
            else:
                head.next = None

            continue

        head.next = head.next.next

    return new_head


if __name__ == '__main__':
    input_head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
    output_head = merge_nodes(input_head)
    output_nodes = []
    while output_head:
        output_nodes.append(output_head.val)
        output_head = output_head.next
    print(f'Output linked list after merge between zeroes - {output_nodes}')  # [4, 11]
