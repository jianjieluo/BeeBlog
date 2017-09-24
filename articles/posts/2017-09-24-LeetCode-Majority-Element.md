@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Majority Element

> Difficulty: Easy

> Week 3

## Description

Given an array of size n, find the majority element. The majority element is the element that appears more than $⌊ n/2 ⌋$ times.

You may assume that the array is non-empty and the majority element always exist in the array.

[原题链接](https://leetcode.com/problems/majority-element/description/)

## Personal Solution

因为所符合条件的数一定是要出现多于$⌊ n/2 ⌋$次，先用`sort`函数进行排序，然后从头开始迭代，但是每次迭代只检查a[i]和a[i + ⌊ n/2 ⌋]两个数是否相等，如果是的话那么这个就是众数了。这个解法可能不具有一般性**，实际上这道题目提供的评测数据没有两个总数相同的数出现，并且也只有一个众数出现的次数超过了⌊ n/2 ⌋次**，所以这个算法可以成功通过此题。

```cpp
#include <algorithm>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int majornums = n / 2;
        int bound = n - majornums;
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < bound; ++i) {
            if (nums[i] == nums[i+majornums]) {
                return nums[i];
            }
        }
        
        return -1;
    }
};
```