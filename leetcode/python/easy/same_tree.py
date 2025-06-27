# task number - 100
# topics - tree, depth-first-search, breadth-first-search, binary tree


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def same_tree(p: Node = None, q: Node = None) -> bool:
    if p is None and q is None:
        return True

    if not (p and q):
        return False

    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)


if __name__ == '__main__':
    input_p = Node(val=1, left=Node(val=2), right=Node(val=3))
    input_q = Node(val=1, left=Node(val=2), right=Node(val=3))
    print(f'Are trees same - {same_tree(p=input_p, q=input_q)}')  # true

    input_p = Node(val=1, left=Node(val=2))
    input_q = Node(val=1, right=Node(val=2))
    print(f'Are trees same - {same_tree(p=input_p, q=input_q)}')  # false

    input_p = Node(val=1, left=Node(val=2), right=Node(val=1))
    input_q = Node(val=1, left=Node(val=1), right=Node(val=1))
    print(f'Are trees same - {same_tree(p=input_p, q=input_q)}')  # false
