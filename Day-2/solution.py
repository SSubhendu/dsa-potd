from ast import Dict, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countGoodSubtrees(root: TreeNode, k: int) -> int:
    def postorder(node: TreeNode) -> Tuple[Dict[int, int], int]:
        if not node:
            return {}, 0
        left_counts, left_distinct = postorder(node.left)
        right_counts, right_distinct = postorder(node.right)
        counts = merge_counts(left_counts, right_counts, node.val)
        distinct = len(counts)
        if distinct <= k:
            nonlocal ans
            ans += 1
        return counts, distinct

    def merge_counts(counts1: Dict[int, int], counts2: Dict[int, int], val: int) -> Dict[int, int]:
        counts = counts1.copy()
        for key, value in counts2.items():
            if key in counts:
                counts[key] += value
            else:
                counts[key] = value
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
        return counts

    ans = 0
    postorder(root)
    return ans
