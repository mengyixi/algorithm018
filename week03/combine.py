class Solution:
    @staticmethod
    def combine1(n, k):
        """
        回溯
        n与每一个元素组合，当组合长度为k时，换掉组合中的元素。所以是很明显的回溯。
        所以终止条件是当前的组合长度为k时。
        在当前组合的长度小于k时，进行回溯。即下探，递归。
        1. 判断终止条件
        2. 业务逻辑
        3. 下探
        4. 清除多余的值
        :param n:
        :param k:
        :return:
        """
        nums = [i for i in range(1, n + 1)]
        res = []

        def backtrace(nums_b, curr_comb, index):
            if len(curr_comb) == k:
                res.append(curr_comb[:])
                return
            for i in range(index, n):
                curr_comb.append(nums[i])
                backtrace(nums_b[index:], curr_comb, i + 1)
                curr_comb.pop()

        if n == 0 or k == 0:
            return res
        backtrace(nums, [], 0)
        return res

    @staticmethod
    def combine2(n, k):
        """
        分治递归。时间复杂度为O(2^(n+k))。
        1.当n小于k，n小于1，或是k为0，n等于k时，终止递归。
        2.递归。
        3.合并下探的结果
        :param n:
        :param k:
        :return:
        """
        if n < k or n < 1:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        ans1 = Solution.combine2(n - 1, k - 1)
        ans2 = Solution.combine2(n - 1, k)
        if ans1:
            for i in ans1:
                i.append(n)
        return ans1 + ans2
