class Solution:
    @staticmethod
    def reverse_str(s, k):
        output = ''
        for i in range(0, len(s), 2 * k):
            tmp = s[i:i + k]
            tmp = tmp[::-1] + s[i + k:i + 2 * k]
            output += tmp
        return output
