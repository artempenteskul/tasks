# task number - 876


class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node


def middle_of_linked_list(head: ListNode) -> ListNode or None:
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    while first and second:
        first = first.next
        second = second.next.next if second.next else None

    return first


if __name__ == '__main__':
    node_2 = ListNode(val=3)
    node_1 = ListNode(val=2, next_node=node_2)
    head = ListNode(val=1, next_node=node_1)

    middle_node = middle_of_linked_list(head)
    print(f'Middle node value - {middle_node.val}')
