@(Coding Language & Algorithm)[LeetCode]

# LeetCode kth Largest Element in an Array

> Difficulty: Medium

> Week 3

## Description

Find the $k^{th}$ largest element in an unsorted array. Note that it is the $k^{th}$ largest element in the sorted order, not the $k^{th}$ distinct element.

For example,
Given `[3,2,1,5,6,4]` and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

[原题链接](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

## Personal Solution

朴素算法自然可以是排序在直接下标读取，**但是最近课上讲的以分治算法为主，所以强迫自己使用递归的分治算法作为练习。**

这道题目是分治算法思想里面的经典题目，**分治思想是要把一个问题分解成为几个子问题，然后子问题和原来的问题本质上是一类的问题，只是规模变小了而已。**因为我们只需要求出数组中的第k大数，所以可能并不需要对数组内的所有元素都进行排序。

借鉴快速排序的思想，每一次迭代选取一个参照值pivot，通过一次遍历把数组分隔成三个部分：
1. 所有比pivot小的数组成的数组a1
2. pivot这个数
3. 所有比pivot大的数组组成的数组a2

则：
1. 若k < len(a2) + 1, 则我们下一次迭代只需要在a2里面找第k大数即可
2. 若k = len(a2) + 1, 则pivot就是我们所有找的值
2. 若k > len(a2) + 1, 则我们下一次迭代只需要在a1里面找第k-len(a2)大数即可

## First AC Version

第一次ac的版本主要借鉴快排思想，思考分治过程。**每次选择问题数组的最后一个数作为pivot，通过下标处理来表示每次迭代问题数组的大小范围，而不是生成新的子数组。**有一些用时间换空间的感觉，加上递归调用，程序跑的速度并不算快。整体代码非常简洁易懂，实现过程中的主要问题是要弄清出各个下标整数所代表的意义以及它们运算后的意义即可。

```cpp
#include <algorithm>
// 此题目不考虑数组里面有重复的数存在

class Solution {
public:  
    int findKthLargest(vector<int>& nums, int k) {
        return kth(nums, k, 0, nums.size());
    }
    
    int kth(vector<int>& nums, int k, int st, int ed) {
        int pivot = nums[ed-1];
        int storeIndex = st;
        
        for (int i = st; i < ed-1; ++i) {
            if (nums[i] < pivot) {
                swap(nums[i], nums[storeIndex++]);
            }
        }
        swap(nums[storeIndex], nums[ed-1]);
        
        if (ed - storeIndex == k) return nums[storeIndex];
        
        if (ed - storeIndex > k) {
            return kth(nums, k, storeIndex+1, ed);
        } else {
            return kth(nums, k-ed+storeIndex, st, storeIndex);
        }
    }
};
```