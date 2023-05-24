# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return

        answer = []
        q = deque()
        q.append(root)

        while q:
            values = []

            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    values.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if values:
                answer.append(values)

        return answer


    