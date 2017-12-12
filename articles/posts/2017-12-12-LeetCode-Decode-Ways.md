@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Decode Ways

> Difficulty: Medium
>
> Week 15

## Description

（原题91）

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message `"12"`, it could be decoded as `"AB"` (1 2) or `"L"` (12).

The number of ways decoding `"12"` is 2.

[原题链接](https://leetcode.com/problems/decode-ways/description/)

## Personal Solution

考虑动态规划的方法来解决这个问题，用`dp[i]`来表示字符串前i个位置所有的可能decode组合。则对于一般情况来看，`dp[i]`就有可能是前i-1个字符的组合情况加上前i-2个字符（如果倒数两个字符解码合法）的组合情况，即对于一般情况有状态转移方程：

1. 若s[i-1]s[i]的组合合法：

$$
dp[i] = dp[i-1] + dp[i-2]
$$

1. 若s[i-1]s[i]的组合不合法：

2. $$
   dp[i] = dp[i-1] + 0
   $$


但是实际上并没有那么简单，需要考虑到`"0"`的情况。对于第i个字符是`0`的情况，由于`0`是不能单独来进行解码的，所以必须要考虑第i-1个字符的情况：

1. 如果这两个字符的组合不合法，那么`0`就不可能在组成合法的解码，此时的`dp[i]`就应该为0.
2. 如果这两个字符的组合合法，那么该`0`就只能和第i-1个字符绑定住解码，此时的dp[i]就应该为`dp[i-2]`.

综上所述，在进行一般情况的动态规划的递归过程中同时注意考虑`0`的情况即可。

**同时，对于前两位的迭代开始情况，需要特殊化进行判断处理。**



## First AC Version

```cpp
class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        if (n == 0) return 0;
        
        vector<int> dp(n, 0);
        
        // 初始化s前2个字符的状态
        if (is1valid(s, 0)) {
            dp[0] = 1;
            if (is1valid(s, 1) && !is2valid(s, 1)) {
                dp[1] = 1;
            }
            else if (is1valid(s, 1) && is2valid(s, 1)) {
                dp[1] = 2;
            }
            else if (!is1valid(s, 1) && is2valid(s, 1)) {
                dp[1] = 1;
            }
            else if (!is1valid(s, 1) && !is2valid(s, 1)) {
                dp[1] = 0;
            }
        }
        
        for (int i = 2; i < n; ++i) {
            if (is1valid(s, i)) {
                int temp = (is2valid(s, i)) ? dp[i-2] : 0;
                dp[i] = dp[i-1] + temp;  
            } else {
                // s[i] 为0，s[i-1]强制和它匹配
                dp[i] = (is2valid(s, i)) ? dp[i-2] : 0;
            }

        }
        cout << n-1 << dp[n-1] << endl;
        return dp[n-1];
    }
    
    bool is1valid(const string& s, const int i) {
        // 判断当前单字符i是否合法（1-9）
        return (s[i] != '0');
    }
    
    bool is2valid(const string& s, const int i) {
        // 判断i位置前2个字符是否合法（10-26）
        if (s[i-1] > '2' || s[i-1] < '1') return false;
        if (s[i-1] == '2' && s[i] > '6') {
            return false;
        }
        return true;
    }
};
```