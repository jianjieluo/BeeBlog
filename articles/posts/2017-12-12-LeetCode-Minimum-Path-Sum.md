@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Minimum Path Sum

> Difficulty: Medium
>
> Week 15

## Description

（原题64）

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**	

```
[[1,3,1],
 [1,5,1],
 [4,2,1]]
```

Given the above grid map, return `7`. Because the path 1→3→1→1→1 minimizes the sum.

[原题链接](https://leetcode.com/problems/minimum-path-sum/description/)

## Personal Solution

这道题目也是常见的有关走迷宫的动态规划的题目。如果需要求最短路径，则可以知道只走下和右才有可能走出最短路径。因此初始化好矩阵的第一行和第一列的情况后，对于一般的情况，有状态转移方程：
$$
grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
$$
最后返回的结果就应该是：$grid[m-1][n-1]$

## First AC Version

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = 1; i < m; ++i) {
            grid[i][0] += grid[i-1][0];
        }
        for (int j = 1; j < n; ++j) {
            grid[0][j] += grid[0][j-1];
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[m-1][n-1];
    }
    
    int min(const int a, const int b) {
        return (a < b) ? a : b;
    }
};
```