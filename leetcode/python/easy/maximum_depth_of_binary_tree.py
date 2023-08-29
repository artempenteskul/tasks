# task number - 104


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# example of bfs algo (uses queue)

def count_max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth = 0
    queue = [root]

    while queue:
        depth += 1
        level_size = len(queue)

        for i in range(level_size):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(count_max_depth(root))  # 3
