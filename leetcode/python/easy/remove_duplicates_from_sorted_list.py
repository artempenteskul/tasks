# task number - 83


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next

        cur = cur.next

    return head


if __name__ == '__main__':
    l1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(2)))
    l2 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3)))))
    l3 = ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0)))

    res1 = delete_duplicates(l1)
    res2 = delete_duplicates(l2)
    res3 = delete_duplicates(l3)

    results1 = []
    while res1:
        results1.append(res1.val)
        res1 = res1.next

    print(results1)  # [1, 2]

    results2 = []
    while res2:
        results2.append(res2.val)
        res2 = res2.next

    print(results2)  # [1, 2, 3]

    results3 = []
    while res3:
        results3.append(res3.val)
        res3 = res3.next

    print(results3)  # [0]
