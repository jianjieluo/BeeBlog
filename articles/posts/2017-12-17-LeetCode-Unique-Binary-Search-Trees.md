@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Unique Binary Search Trees

> Difficulty: Medium
>
> Week 15

## Description

（原题96）

Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1...*n*?

For example,
Given *n* = 3, there are a total of 5 unique BST's.

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

[原题链接](https://leetcode.com/problems/unique-binary-search-trees/description/)

## Personal Solution

​考虑动态规划的方法来解决这个问题，找规律，对于一字排开的数字，从左到右每次选一个出来当做根节点，则该根节点的组成的BST数就是起左子树的组合数乘以右子树的组合数，再全部相加。



​用`dp[i]`表示i个按顺序的序列组成的BST数的数目，最后的结果就应该是`dp[n]`，则：

`dp[0] = 1; dp[1] = 1;`

` dp[k] = dp[0] * dp[k-0-1] + dp[1] * dp[k-1-1] + ... + dp[k-2] * dp[1] + dp[k-1] * dp[0];`

​因为这里并不需要关注子问题区间的左右边界而是只需要关注子问题区间的长度即可，所以一些之前计算出来的结果可以为后面的计算所使用。

### First AC Version

```cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 1);
        
        for (int k = 2; k < n + 1; ++k) {
            int temp = 0;
            for (int i = 0; i < k; ++i) {
                temp += dp[i] * dp[k-i-1];
            }
            dp[k] = temp;
        }
        return dp[n];
    }
};
``````