class Solution:
    @staticmethod
    def lemonade_change(bills):
        """
        贪心算法。时间复杂度O(n)，空间复杂度O(n)。
        找零，判断当前各个面值的纸币是否小于0，是的话函数停止运行，返回false
        如果能够运行到函数最后，返回true
        :param bills:
        :return:
        """
        if len(bills) == 0:
            return True
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif bill == 20 and ten == 0:
                five -= 3
            else:
                five -= 1
                ten -= 1
            if five < 0 or ten < 0:
                return False
        return True


test_cases = [
    {"input": [5, 5, 10], "expect": True},
    {"input": [10, 10], "expect": False},
    {"input": [5, 5, 5, 10, 20], "expect": True},
    {"input": [5, 5, 10, 10, 20], "expect": False},
    {"input": [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5], "expect": True},
]

for case in test_cases:
    assert (Solution.lemonade_change(case['input']) is case['expect'])

print("pass!")
