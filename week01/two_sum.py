"""
解题思路：
嵌套循环。一次循环，把当前的元素的差值存入数组中，在下一次的循环中去遍历临时数组，当前的元素是否命中差值，命中则存在并返回。
一次循环。和嵌套循环的思路类似，但是借助哈希表降低了复杂度。
"""
class Solution:
    @staticmethod
    def two_sum_way1(nums, target):
        temp = {}
        for index, num in enumerate(nums):
            if temp.get(target - num) is not None:
                return [index, temp.get(target - num)]
            temp[num] = index
        return

    @staticmethod
    def two_sum_way2(nums, target):
        temp = []
        i = 0
        for item in nums:
            j = 0
            for ele in temp:
                if ele == item:
                    return [j, i]
                else:
                    j = j + 1
            temp.append(target - item)
            i = i + 1
        return []


test_cases = [
    {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expect": [0, 1], "expect2": [1, 0]},
    {"input": {"nums": [3, 2, 4], "target": 6}, "expect": [1, 2], "expect2": [2, 1]},
    {"input": {"nums": [3, 2, 3], "target": 6}, "expect": [0, 2], "expect2": [2, 0]},
    {"input": {"nums": [-3, 4, 3, 90], "target": 0}, "expect": [0, 2], "expect2": [2, 0]}
]

for case in test_cases:
    res1 = Solution.two_sum_way1(case['input']['nums'], case['input']['target'])
    assert (res1 == case['expect'] or res1 == case['expect2'])
    res2 = Solution.two_sum_way2(case['input']['nums'], case['input']['target'])
    assert (res2 == case['expect'] or res2 == case['expect2'])
