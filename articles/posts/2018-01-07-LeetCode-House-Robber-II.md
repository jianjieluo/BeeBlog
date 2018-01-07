@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-House Robber II

> Difficulty: Medium
>
> Week 18

## Description

（原题 213）

**Note:** This is an extension of [House Robber](https://leetcode.com/problems/house-robber/).

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

[原题链接](https://leetcode.com/problems/house-robber-ii/description/)

## Personal Solution

继续用动态规划的思路去考虑即可，对于每个房子，`a[0][i]`表示i房子不抢拿到的最大利润，`a[1][i]`表示i房子抢拿到的最大利润。

动态转移方程如下：

```cpp
a[0][i] = max(a[0][i-1], a[1][i-1]);
a[1][i] = a[0][i-1] + nums[i];
```

因为这里， 房子是首尾相连的，只要分开思考两个情况即可，一个是第一个房子抢，一个是第一个房子不抢，这样子进行两次动态规划a和b，选出4个值之中的最大值即可。要注意的是**两次动态规划的范围是不同的**。



### First AC Version

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> a[2];
        vector<int> b[2];
        
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        a[0].resize(n);
        a[1].resize(n);
        b[0].resize(n);
        b[1].resize(n);
        
        // first not robbed
        a[0][1] = 0;
        a[1][1] = nums[1];
        for (int i = 2; i < n; ++i) {
            a[0][i] = max(a[0][i-1], a[1][i-1]);
            a[1][i] = a[0][i-1] + nums[i];
        }
        
        // first robbed
        b[0][0] = 0;
        b[1][0] = nums[0];
        for (int i = 1; i < n-1; ++i) {
            b[0][i] = max(b[0][i-1], b[1][i-1]);
            b[1][i] = b[0][i-1] + nums[i];
        }
        
        return max(max(a[0][n-1], a[1][n-1]), max(b[0][n-2], b[1][n-2]));
    }
    
    int max(const int a, const int b) {
        return a<b ? b : a;
    }
};
```