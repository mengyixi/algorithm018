"""
解题思路：
寻找相似性。两个升序链表，合并成一个链表，可以理解成每一次都是比较链表1和链表2中，
未合并的第一个节点的值的大小 ，然后将值较小的节点的next指向值较大的节点。每一步都是相似的，所以可以考虑采用递归的方式。
第一步是寻找递归结束的方式，当前的两个节点中任意一节点指向空，即结束，直接返回指向空的节点。
第二步是处理逻辑，给两个节点做值的大小的判断。
第三步是向下递归。
第四步是修改较小节点指向的节点并返回。
由于两天前做过类似的题目(爬楼梯)，所以看到该题是很快就找到了思路。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val >= l2.val:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2
        else:
            l1.next = self.merge_two_lists(l2, l1.next)
            return l1
