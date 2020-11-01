"""
N叉树的层序遍历
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def level_order(root):
        """
        递归。把每一次的函数执行的结果放入同一个列表中。
        :param root:
        :return:
        """
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []
        if root is not None:
            traverse_node(root, 0)
        return result
