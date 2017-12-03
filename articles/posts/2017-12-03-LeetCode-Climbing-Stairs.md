@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Climbing Stairs

> Difficulty: Easy

> Week 13

## Description
(原题70)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

[原题链接](https://leetcode.com/problems/climbing-stairs/description/)

## Personal Solution

动态规划的简单题目。令一个数组`a[i]`表示有i个台阶的时候可以走的方法数。那么当前的走的方法数应该是i-1级阶梯走的方法数后再走一步，或者i-2级阶梯走的方法数后再走两步。状态转移方程如下：

$$
a[i] = a[i-2] + a[i-1]
$$

在实现的过程中注意好一开始n<2的边界问题即可。

## First AC Version

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> a(n+1, 0);
        
        a[0] = 1;
        a[1] = 1;
        if (n<2) return 1; 
        
        a[2] = 2;
        for (int i = 3; i < n+1; ++i) {
            a[i] = a[i-1] + a[i-2];
        }
        return a[n];
    }
};
```