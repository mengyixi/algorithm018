"""
二叉树先序遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def preorder_traversal_1(root):
        """
        颜色标记法
        新节点标记为白色，已访问的节点置为灰色
        如果是白色节点，置灰，将右子节点,左子节点,根节点依次入栈
        如果节点为灰色，输出节点的值
        :param root:
        :return:
        """
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((white, node.right))
                stack.append((white, node.left))
                stack.append((gray, node))
            else:
                res.append(node.val)
        return res

    def preorder_traversal_2(self, root):
        """
        根节点 + 左子树递归 + 右子树递归
        :param root:
        :return:
        """
        if root is None:
            return []
        res = [root.val]
        left_list = self.preorder_traversal_2(root.left)
        right_list = self.preorder_traversal_2(root.right)
        return res + left_list + right_list
