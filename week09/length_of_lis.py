class Solution:
    @staticmethod
    def length_of_lis(nums):
        n = len(nums)

        if n < 2:
            return n
        tail = [nums[0]]
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left = 0
            right = len(tail) - 1
            while left <= right:
                mid = (left + right) // 2
                if tail[mid] >= nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            tail[left] = nums[i]
        return len(tail)
