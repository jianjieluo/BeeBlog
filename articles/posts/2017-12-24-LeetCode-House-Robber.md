@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-House Robber

> Difficulty: Easy
>
> Week 16

## Description

（原题198）

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

[原题链接](https://leetcode.com/problems/house-robber/description/)

## Personal Solution

用动态规划的思路去考虑即可，用`dp[i]`表示到第i个房子抢或者不抢可以拿到的最大的收益，最后选择`dp`数组中的最大值即可。

动态转移方程如下：

```
dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i], dp[i-1])
```

### First AC Version

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        
        int currMax = 0;
        
        for (int i = 0; i < n; ++i) {
            if (i == 0 || i == 1) {
                dp[i] = nums[i];
            } else if (i == 2) {
                dp[i] = max(dp[i-2]+nums[i], dp[i-1]);
            } else {
                dp[i] = max(max(dp[i-2], dp[i-3]) + nums[i], dp[i-1]);
            }
            if (currMax < dp[i]) currMax = dp[i];
        }
        return currMax;
    }
    
    int max(const int a, const int b) {
        return (a < b) ? b : a;
    }
};
```

