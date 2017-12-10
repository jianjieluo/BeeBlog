# LeetCode-Wildcard Matching



> Difficulty: hard
>
> Week 14



## Description



(原题44)



Implement wildcard pattern matching with support for `'?'` and `'*'`.



```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
```



[原题链接](https://leetcode.com/problems/wildcard-matching/description/)



## Personal Solution

此题和[leetcode第10题](https://longjj.com/2017/11/26/LeetCode-Regular-Expression-Matching/)其实比较类似，动态规划的表示方式可以借鉴这一题，所不同的只是状态转移的条件有所不同。

`dp[i][j]`表示msg`s`的前i个字符可以和patten `p`的前j个字符相匹配。当i=0时，`s`是空字符串。

那么最终的结果就应该是`dp[m][n]`。



1. 初始化矩阵的第一行和第一列。当s为空时，需要妥善处理p的情况，当p一直是'\*'的时候`p[0][j]`才是真，否则一出现不是'*'的字符，`p[0][j]`以后就一定为假.



对于一般情况的状态转移，对于`dp[i][j]`, 主要考虑`p[j-1]`的值：

1. 当`p[j-1]`不是特殊字符`?`和`*`的时候。 ` dp[i][j] = dp[i-1][j-1] && (p[j-1] == s[i-1]);`
2. 当`p[j-1]`是`?`的时候。`dp[i][j] = dp[i-1][j-1];`
3. 当`p[j-1]`是`*`的时候，因为'\*'可以匹配任意字串，所以必须在该'*'前的子模式一定可以匹配某个前子串，否则就一定会匹配不成功。则`dp[i][j] = dp[i][j-1] || dp[i-1][j-1] || dp[i-2][j-1] || ... || dp[0][j-1];`



## First AC Version



```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
        
        dp[0][0] = true;
        if (p[0] == '*') {
            // 初始的第一行和第一列很重要！当s为空时，需要妥善处理p的情况，当p一直是'*'的时候p[0][j]才是真，
            // 否则一出现不是'*'的字符，p[0][j]以后就一定为假.
            for (int j = 1; j < n + 1; ++j) {
                dp[0][j] = dp[0][j-1] && (p[j-1] == '*');
            }
            for (int i = 1; i < m + 1; ++i) {
                dp[i][1] = true;
            }
        }
        
        for (int i = 1; i < m+1; ++i) {
            for (int j = 1; j < n+1; ++j) {
                // 当p[j-1]不是特殊字符的时候
                if (p[j-1] != '?' && p[j-1] != '*') {
                    dp[i][j] = dp[i-1][j-1] && (p[j-1] == s[i-1]);
                } else {
                    if (p[j-1] == '?') {
                        dp[i][j] = dp[i-1][j-1];
                    } else if (p[j-1] == '*') {
                        // 因为'*'可以匹配任意字串，所以必须在该'*'前的子模式一定可以匹配某个前子串，
                        // 否则就一定会匹配不成功。
                        // 即：dp[i][j] = dp[i][j-1] || dp[i-1][j-1] || dp[i-2][j-1] || ... || dp[0][j-1];
                        for (int k = 0; k <= i; ++k) {
                            // 此处k从0还是从1开始没有关系
                            // 因为若dp[0][j-1]为true的时候，p[0]到p[j-1]都一定为'*', dp[1][j-1]也一定为true 
                            if (dp[k][j-1]) {
                                dp[i][j] = true;
                                break;
                            }
                        }
                    }
                }
            }
        }
        return dp[m][n];
    }
};
```

