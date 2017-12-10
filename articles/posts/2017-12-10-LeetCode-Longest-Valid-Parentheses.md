# LeetCode-Longest Valid Parentheses



> Difficulty: hard
>
> Week 14



## Description



(原题32)



Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

For `"(()"`, the longest valid parentheses substring is `"()"`, which has length = 2.

Another example is `")()())"`, where the longest valid parentheses substring is `"()()"`, which has length = 4.



[原题链接](https://leetcode.com/problems/longest-valid-parentheses/description/)



## Personal Solution



首先这里记录一下括号匹配问题的一些常见的性质：

1. 使用栈进行匹配，当整个字符串按顺序输入完了之后，栈里面的元素就是没有匹配上的括号，而且其相对顺序不变。
2. 对于一个合法的括号字符串，若当前的字符为')', 则与该字符匹配的左括号的位置必然在`i - longest[i-1] - 1`这个位置上，其中`longest[i]`表示的是前i个字符串（包括了第i个字符）的最长合法匹配的长度。



括号匹配，最基本的想法是使用栈来进行操作，这里用一个动态规划的方法来解决这个问题。我们使用`A[i]`表示的是前i个字符串（包括了第i个字符）的最长合法匹配的长度。

1. 若`s[i]`为`(`，`A[i]`为0。
2. 若`s[i]`为`)`，只需要根据上面的第2条性质判断一下在`i - A[i-1] - 1`这个位置是不是存在`(`和它匹配即可
   1. 如果是的话，`A[i]`的值将是在`A[i-1]`的基础上加2，并且再加上`i - A[i-1] - 1`之前的合法最长长度即可。
   2. 如果不是的话则为0。



**最后结果应该是A这个数组里面的最大值**。

为了处理边界情况，需要在操作前加上`i-A[i-1]-1 >= 0`的这个判断条件。



## First AC Version



```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length();
        int currMax = 0;
        vector<int> A(n, 0);
        for (int i = 0; i < n; ++i) {
            if (s[i] == ')' && (i-A[i-1]-1) >= 0) {
                if (s[i-A[i-1]-1] == '(') {
                    A[i] = A[i-1] + 2 + A[i-A[i-1]-2];
                    if (currMax < A[i]) currMax = A[i];
                }
            }
        }
        return currMax;
    }
};
```

