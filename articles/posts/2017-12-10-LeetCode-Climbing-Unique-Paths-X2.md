@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Climbing Unique Paths X2

> Difficulty: Medium x 2

> Week 14

## Description 1 
(原题62)

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

[原题链接](https://leetcode.com/problems/unique-paths/description/)

### Personal Solution

非常基础的动态规划题目，到每个点的路径数可以由下面两个数相加组成：
1. 到左邻点的路径数（再往右走一步）
2. 到上邻点的路径数（再往下走一步）

若以`dp[i][j]`表示到达点`(i, j)`的路径数，则状态转移方程则是：

$$
dp[i][j] = dp[i-1][j] + dp[i][j-1];
$$

### First AC Version

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                // 到左邻点的路径数（再往右走一步）+
                // 到上邻点的路径数（再往下走一步）
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```

## Description 2
(原题63)

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

```

The total number of unique paths is 2.

[原题链接](https://leetcode.com/problems/unique-paths-ii/description/)

### Personal Solution

在上一题的基础上，我们需要对有障碍的点进行一些特殊的处理。

1. 在地图的最左边，当存在 i 使得`(i, 0)`点是有障碍的情况下，则`(k, 0), k > i`都不可达，`dp[k][0]`为0
2. 同理，在地图的最上边，当存在 j 使得`(0, j)`点是有障碍的情况下，则`(0, k), k > j`都不可达，`dp[0][k]`为0
3. 地图上所有有障碍的点`dp[i][j]`都为0

处理完上述的特殊情况，一般情况的状态转移方程和上一题是一样的：

$$
dp[i][j] = dp[i-1][j] + dp[i][j-1];
$$

### First AC Version

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        for (int i = 0; i < m; ++i) {
            if (obstacleGrid[i][0] == 1) {
                for (int k = i; k < m; ++k) {
                    dp[k][0] = 0;
                }
                break;
            }
        }
        for (int j = 0; j < n; ++j) {
            if (obstacleGrid[0][j] == 1) {
                for (int k = j; k < n; ++k) {
                    dp[0][k] = 0;
                }
                break;
            }
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                    continue;
                }
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```