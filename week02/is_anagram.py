import collections


class Solution:
    @staticmethod
    def is_anagram_1(s, t):
        """
        通过哈希表来统计s中每个元素出现的次数并放入哈希表中
        循环t并与哈希表中的键与值做对比
        :param s:
        :param t:
        :return:
        """
        if t == "" and s != "":
            return False
        hash_map = collections.Counter(s)
        for i in t:
            if i not in s or hash_map[i] == 0:
                return False
            hash_map[i] = hash_map[i] - 1
        for idx, nums in hash_map.items():
            if nums > 0:
                return False
        return True

    @staticmethod
    def is_anagram_2(s, t):
        """
        统计两个字符串每个元素出现的次数
        然后做对比
        :param s:
        :param t:
        :return:
        """
        s_hash = dict(collections.Counter(s))
        t_hash = dict(collections.Counter(t))
        for idx, nums in s_hash.items():
            if t_hash.get(idx) != nums:
                return False
        if len(set(s_hash.keys()) ^ set(t_hash.keys())) > 0:
            return False
        return True

    @staticmethod
    def is_anagram_3(s, t):
        """
        对两个字符串排序
        然后判断两个排序后的字符串是否相等
        :param s:
        :param t:
        :return:
        """
        s_l = len(s)
        t_l = len(t)
        if s_l != t_l:
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if s != t:
            return False
        return True


test_cases = [
    {"input": {"s": "ab", "t": "a"}, "expect": False},
    {"input": {"s": "anagram", "t": "nagaram"}, "expect": True},
    {"input": {"s": "rat", "t": "t"}, "expect": False},
    {"input": {"s": "", "t": ""}, "expect": True},
    {"input": {"s": "a", "t": "ab"}, "expect": False},
    {"input": {"s": "a", "t": "b"}, "expect": False}
]

for case in test_cases:
    assert (Solution.is_anagram_1(case['input']['s'], case['input']['t']) is case['expect'])
    assert (Solution.is_anagram_2(case['input']['s'], case['input']['t']) is case['expect'])
    assert (Solution.is_anagram_3(case['input']['s'], case['input']['t']) is case['expect'])
