@(Coding Language & Algorithm)[LeetCode]

[toc]

# LeetCode-Regular Expression Matching

> Difficulty: Hard

> Week 12

## Description 

Implement regular expression matching with support for `'.'` and `'*'`.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:

```
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```

[原题链接](https://leetcode.com/problems/regular-expression-matching/description/)

## Personal Solution

最近需要开始加强动态规划题目的练习了。
此题可以用动态规划的思路来思考。首先要思考一个二维矩阵的表现形式来模拟这个问题。我们可以定义：

`dp[i][j]`表示msg`s`的前i个字符可以和patten `p`的前j个字符相匹配。当i=0时，`s`是空字符串。

那么最终的结果就应该是`dp[m][n]`

动态规划的重点是如何把一个问题递归分成一些比较小的子问题。不难想到若一个串可以和pattern匹配，那么它的子串也应该可以和pattern的某个子串匹配，由此可以想出状态转移情况：

1. dp[0][0] = true
2. i > 0, j == 0 时，dp[i][j] = false
3. j > 0 时：
	4. 若p[j-1]不为`.`或`*`时：`dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1]);`
	5. 若p[j-1]为`.`时：`dp[i][j] = dp[i-1][j-1];`
	6. 若p[j-1]为`*`时，需要通过p[j-1]和p[j-2]的情况来判断：
		7. 匹配0个或1个时：`dp[i][j-1] || dp[i][j-2]`为真
		8. 匹配2个以上时：`(p[j-2]==s[i-1] || p[j-2]=='.') && dp[i-1][j]`为真

具体时实现上来说，需要考虑数组越界的问题，所以之前只在纸笔上思考问题还是需要有额外的考虑的，具体的做法就是在每个状态转移式上面加上`i > 0`的这些限制。

## First AC Version

```cpp
#include <vector>
using namespace std;

class Solution {
public:
bool isMatch(const string& s, const string& p) {
    int m = s.length();
    int n = p.length();
    
    vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
    dp[0][0] = true;
    
    for (int i = 0; i < m + 1; ++i) {
        for (int j = 1; j < n + 1; ++j) {
            if (p[j-1] != '.' && p[j-1] != '*') {
                if (i > 0) {
                    dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1]);
                }
            } else if (p[j-1] == '.') {
                if (i > 0) {
                    dp[i][j] = dp[i-1][j-1];
                }
            } else if (j > 1 && p[j-1] == '*') {
                if (dp[i][j-1] || dp[i][j-2]) {
                    dp[i][j] = true;
                } else if (i>0 && (p[j-2]==s[i-1] || p[j-2]=='.') && dp[i-1][j]) {
                    dp[i][j] = true;
                }
            }
        }
    }
    
    return dp[m][n];
}
};
```