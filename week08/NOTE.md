#学习笔记
##冒泡排序
```python
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```
##选择排序
```python
def select_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
```
##插入排序
```python

```
##希尔排序
```python

```
##归并排序
```python

```
##快速排序
```python

```
##堆排序
```python

```
##计数排序
```python

```
##桶排序
```python

```
##基数排序
```python

```
