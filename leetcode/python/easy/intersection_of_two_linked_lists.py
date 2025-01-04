# task number - 160
# topics - hash table, linked list, two pointers


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node

    def __repr__(self) -> str:
        return f'ListNode({self.val})'


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode or None:
    visited = set()

    while head_a or head_b:
        for head in (head_a, head_b):
            if head:
                if head in visited:
                    return head
                else:
                    visited.add(head)

        head_a = head_a.next if head_a else head_a
        head_b = head_b.next if head_b else head_b

    return None


if __name__ == '__main__':
    input_intersection_node = ListNode(val=2, next_node=ListNode(4))
    input_head_a = ListNode(val=1, next_node=ListNode(val=9, next_node=ListNode(1, next_node=input_intersection_node)))
    input_head_b = ListNode(val=3, next_node=input_intersection_node)
    print(f'Intersection node value of two input heads - {get_intersection_node(input_head_a, input_head_b)}')  # ListNode(2)

    input_head_a = ListNode(val=2, next_node=ListNode(val=6, next_node=ListNode(val=4)))
    input_head_b = ListNode(val=1, next_node=ListNode(5))
    print(f'Intersection node value of two input heads - {get_intersection_node(input_head_a, input_head_b)}')  # None
