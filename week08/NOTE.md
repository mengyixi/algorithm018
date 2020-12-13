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
def insertion_sort(nums): 
    for i in range(1, len(nums)): 
        key = nums[i] 
        j = i-1
        while j >=0 and key < nums[j] : 
                nums[j+1] = nums[j] 
                j -= 1
        nums[j+1] = key 
```
##希尔排序
```python
def shell_sort(nums):
    n = len(nums)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j = j - gap
            nums[j + gap] = temp
        gap = int(gap / 2)
    return nums
```
##归并排序
```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    num = int( len(nums) / 2 )
    left = merge_sort(nums[:num])
    right = merge_sort(nums[num:])
    return merge(left, right)

def merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result
```
##快速排序
```python
def quick_sort(nums):      
    if len(nums) >= 2:
        mid = nums[len(nums)//2]
        left, right = [], []
        nums.remove(mid)
        for num in nums:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return nums
```
##堆排序
```python
def heapify(nums, n, i): 
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and nums[i] < nums[l]: 
        largest = l 
    if r < n and nums[largest] < nums[r]: 
        largest = r 
    if largest != i: 
        nums[i],nums[largest] = nums[largest],nums[i]
        heapify(nums, n, largest) 
  
def heap_sort(nums): 
    n = len(nums) 
    for i in range(n, -1, -1): 
        heapify(nums, n, i) 
    for i in range(n-1, 0, -1): 
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0) 
```
##计数排序
```python
def count_sort(nums):
    length = len(nums)
    if length < 2:
        return nums
    max_num = max(nums)
    count = [0] * (max_num + 1)
    for item in nums:
        count[item] += 1
    output = []
    for i in range(max_num + 1):
        for j in range(count[i]):        
            output.append(i)
    return output
```
##桶排序
```python
def bucket_sort(nums):
    temp = [[] for _ in range(len(nums))]
    for item in nums:
        index = int(item * len(nums))
        temp[index].append(item)
    for i in range(len(nums)):
        temp[i].sort()
    index = 0
    for i in range(len(nums)):
        for j in range(len(temp[i])):
            nums[index] = temp[i][j]
            index += 1
    return nums
```
##基数排序
```python
import math
 
def radix_sort(nums, radix=10):
    n = int(math.ceil(math.log(max(nums), radix)))
    bucket = [[] * radix]
    for i in range(1, n+1):
        for val in nums:
            bucket[val%(radix**i)/(radix**(i-1))].append(val)
        del nums[:]
        for each in bucket:
            nums.extend(each)
        bucket = [[] * radix]
```
