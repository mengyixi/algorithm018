class Solution:
    @staticmethod
    def valid_palindrome(s):
        if s == s[::-1]:
            return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                t1 = s[left + 1: right + 1]
                t2 = s[left: right]
                return t1 == t1[::-1] or t2 == t2[::-1]
        return True
