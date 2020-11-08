class Solution:
    def lowest_common_ancestor(self, root, p, q):
        """
        1.当前节点为空 or 等于q or等于p，递归终止。
        2.递归左子树和右子树。
        3.如果左子树和右子树都有结果。即表明pq不在root的同一子树中，结果为root。
          如果左右子树都为空，结果是null。
          如果左子树结果不为空，右子树结果为空，结果是左子树的返回结果。、
          如果右子树结果不为空，左子树结果为空，同理。
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or root == p or root == q:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root
