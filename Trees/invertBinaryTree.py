from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertBinaryTree(self, root : Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root
    
    def printLevelOrder(self, root):
        if not root:
            return 
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

                

            
    
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    solution = Solution()
    invertedTree = solution.invertBinaryTree(root)
    solution.printLevelOrder(invertedTree)


    
        