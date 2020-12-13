class Solution:
    """
    leetcode 242.有效的字母异位词
    link: https://leetcode-cn.com/problems/valid-anagram/
    """
    @staticmethod
    def is_anagram(s, t):
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
