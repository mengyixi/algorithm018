class Solution:
    """
    leetcode 1122.数组的相对排序
    link: https://leetcode-cn.com/problems/relative-sort-array/
    """
    @staticmethod
    def relative_sort_array(arr1, arr2):
        output = []
        not_in_arr2 = []
        for item in arr2:
            for ele in arr1:
                if ele == item:
                    output.append(ele)
        for item in arr1:
            if item not in arr2:
                not_in_arr2.append(item)
        not_in_arr2 = sorted(not_in_arr2)
        output.extend(not_in_arr2)
        return output
