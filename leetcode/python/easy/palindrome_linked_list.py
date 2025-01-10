# task number - 234
# topics - linked list, two pointers, stack, recursion


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None) -> None:
        self.val = val
        self.next = next_node


def is_palindrome(head: ListNode or None) -> bool:
    if not head or not head.next:
        return True

    slow = head
    fast = head

    # find the middle of linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second part
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # compare both parts of linked list
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True


if __name__ == '__main__':
    input_head = ListNode(1, next_node=ListNode(2, next_node=ListNode(2, ListNode(1))))
    print(f'Is input linked list palindrome - {is_palindrome(input_head)}')  # true

    input_head = ListNode(1, next_node=ListNode(2))
    print(f'Is input linked list palindrome - {is_palindrome(input_head)}')  # false

    input_head = ListNode(1, next_node=ListNode(0, next_node=ListNode(1)))
    print(f'Is input linked list palindrome - {is_palindrome(input_head)}')  # true
