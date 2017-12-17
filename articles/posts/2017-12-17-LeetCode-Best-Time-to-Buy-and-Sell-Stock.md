@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Best Time to Buy and Sell Stock

> Difficulty: Easy
>
> Week 15

## Description

（原题121）

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

**Example 1:**
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
```

**Example 2:**
```
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
```

[原题链接](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Personal Solution

此题无疑可以使用暴力枚举求解，遍历`prices`数组，同时遍历第i个前的每一个price，作差运算，取最大值，最后返回即可。复杂度为$O(n^2)$.

### First AC Version

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int n = prices.size();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int temp = prices[i] - prices[j];
                if (temp > res) res = temp;
            }
        }
        return res;
    }
};
```

思考复杂度更低的算法。观察可以发现规律，使用动态规划的方法来解决。`dp[i]`表示在第i天卖出时可以赚到的最多金钱。
则`dp[0] = 0;` 

在第一层循环中，使用一个index来表示这样一个下标，满足以下条件：
1. index < i;
2. dp[index] = 0;
3. 对于任意k < i, dp[k] = 0, 由这些k构成的集合中，index最大。（也就是说index是当前最新的dp[index]为0的下标）

则，对于每一个i，只需要比较当前的price和index下的price，同时视情况更新最大差值`res`和`index`即可。在实际的编程实现中其实不需要把dp数组构造出来。该算法只需要一层循环，复杂度$O(n)$.

**证明：**
假设index不是当前最新的dp[index]为0的下标， 假设j才是当前最新的dp[index]为0的下标。那么，`prices[index] ＞prices[j]` 必然成立，否则`dp[j]` 不为0. 则当前i下如果选择第j天购入的消耗一定比第index天购入的要低，利润更大。所以，循环迭代中每次选择当前最新的dp[index]为0的下标作为比较的对象即可。

### Second AC Version

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int index = 0;
        int res = 0;
        for (int i = 1; i < n; ++i) {
            int temp = prices[i] - prices[index];
            if(temp > 0) {
                res = (res < temp) ? temp : res;
            } else {
                index = i;
            }
        }
        return res;
    }
};
```