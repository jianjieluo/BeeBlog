@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Maximum Subarray

> Difficulty: Easy

> Week 13

## Description
(原题53)

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,
the contiguous subarray` [4,-1,2,1]` has the largest `sum = 6`.

## Personal Solution

动态规划的经典题目，虽然此题可以暴力求解，但是使用动态规划的方法时间复杂度最小。

其中，状态转移方程是:

$$
maxsum[i] = max \{maxsum[i-1] + nums[i], nums[i]\}
$$

最后答案就是遍历后的`maxsum`里面的最大值。

## First AC Solution

```cpp
class Solution {
public:
    int max(const int a, const int b) {
        if (a < b) {
            return b;
        } else {
            return a;
        }
    }
    
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int maxsum[n];
        maxsum[0] = nums[0];
        for (int i = 1; i< n; ++i) {
            maxsum[i] = max(maxsum[i-1] + nums[i], nums[i]);
        }
        int m = nums[0];
        for (int i = 0; i < n; ++i) {
            if (m < maxsum[i]) {
                m = maxsum[i];
            }
        }
        return m;
    }
};
```