# task number - 141


from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    works with additional memory for hash set to check the nodes
    """

    values = set()

    while head:
        if head not in values:
            values.add(head)
        else:
            return True

    return False


def has_cycle1(head: Optional[ListNode]) -> bool:
    """
    works without any additional memory, fast and slow pointer technique
    """

    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

