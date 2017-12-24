@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Maximum Product Subarray

> Difficulty: Medium
>
> Week 16

## Description

（原题152）

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array `[2,3,-2,4]`,
the contiguous subarray `[2,3]` has the largest product = `6`.

[原题链接](https://leetcode.com/problems/maximum-product-subarray/description/)

## Personal Solution

此题和求子数组求和最大有类似的地方，但是乘法需要考虑的地方多一点。用一维`dp[i]`不能表示出最优的情况，因为有可能有两个负数相乘变得更大的情况。所以需要同时记录下当前的最大值和最小值两种情况，使用二维数组`dp[i][2]`,其中`dp[i][0]`表示最大值，`dp[i][1]`表示最小值。



对于遍历到的每一个点：

1. 若`nums[i]`为正数：
   1. 最大值为`dp[i-1][0]` \* 正数 或者 `nums[i]`
   2. 最小值为`dp[i-1][1]` \* 正数 或者 `nums[i]`
2. 若`nums[i]`为负数：
   1. 最大值为`dp[i-1][1]` \* 负数 或者 `nums[i]`
   2. 最小值为`dp[i-1][0]` \* 负数 或者 `nums[i]`



最后选择最大值即可。

### First AC Version

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        
        int currMax = nums[0];
        
        dp[0][0] = dp[0][1] = nums[0];
        for (int i = 1 ; i < n; ++i) {
            if (nums[i] > 0) {
                dp[i][0] = max(dp[i-1][0] * nums[i], nums[i]);
                dp[i][1] = min(dp[i-1][1] * nums[i], nums[i]);
            } else {
                dp[i][0] = max(dp[i-1][1] * nums[i], nums[i]);
                dp[i][1] = min(dp[i-1][0] * nums[i], nums[i]);
            }
            if (currMax < dp[i][0]) currMax = dp[i][0];
        }
        return currMax;
    }
    
    int max(const int a, const int b) {
        return (a < b) ? b : a;
    }
    int min(const int a, const int b) {
        return (a < b) ? a : b;
    }
};
```