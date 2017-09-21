# Median of Two Sorted Arrays

> Difficulty: Hard

> Week 2

## Description

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

Example 2:

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

[原题链接](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

## Personal Solution

朴素算法无疑是把两个排好序的数组合并起来然后再直接取中位数。但是这样子的复杂度是$O(n)$, 而题目要求的是$log(m+n)$，所以我们需要考虑分治算法。

主要的思路是，我们应该要利用好“两个数组已经排好序了”这个条件，并且避免像朴素算法那样去访问两个数组里面的所有元素。题目要求的是求两个排好序的数组的中位数，其实就是一个求两个排好序的数组中的第k小数的特例，其中如果m+n为偶数，那么就求第$(m+n)/2$小数和第$(m+n)/2+1$小数，如果m+n为奇数，那么就求第$(m+n+1)/2$小数。那么，求两个排好序的数组中的第k小数恰好有一个分治算法，我们以此为参考即可。

由于两个数组已经排好序，那么，当k>1的时候，如果我们从两个数组中各自选择一个合适的数作为参考数a,b，$min(a,b)$所在的数组的左边的数(比$min(a,b)$还要小)就可以都舍去，并且进行新一轮分治。为了保证比$min(a,b)$还要小的数的数目比k要小，我们可以选择每次分治的时候采用的下标偏移量是k/2(向下取整)。那么舍弃了数目之后，k变小，数组中的数的数目变小，原问题和处理后的问题本质上是同一个问题，所以可以使用分治。

递归结束的条件：
1. k == 1，这个时候只需要选择两个子数组里面各自第一个元素的最小者即可。
2. k > 1, 但其中一个数组已经都舍弃完了，那么接下来就直接在剩下的排好序的子数组中找好第k小数即可。

这个算法的复杂度是$O(log(k))$，而k的最大值是m+n，那么复杂度就是$O(log(m + n))$。

## Finally AC version

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    double kth(vector<int>& nums1, vector<int>& nums2, int m, int n, int k, int st1 = 0, int st2 = 0) {

        // 看第一数组是否已经取完
        if (st1 == m) {
            return nums2[st2 + k - 1];
        }
        // 看第二数组是否已经取完
        if (st2 == n) {
            return nums1[st1 + k - 1];
        }
        
        if (k == 1) {
            return nums1[st1] > nums2[st2] ? nums2[st2] : nums1[st1];
        }
        
        if (k < 1) {
            cout << "k is less than 1 !" << endl;
            return -1;
        }
        
        int curr = k / 2;
        int newst1 = min(st1 + curr, m);
        int newst2 = min(st2 + curr, n);
        
        
        // 把两个数组中的标准数较小的那个及其左边的数给舍弃，重新进行分治
        if (nums1[newst1 - 1] < nums2[newst2 - 1]) {
            return kth(nums1, nums2, m, n, k - newst1 + st1, newst1, st2);
        } else {
            return kth(nums1, nums2, m, n, k - newst2 + st2, st1, newst2);
        }
    }
    
    
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        int m = nums1.size();
        int n = nums2.size();
        
        if ((m + n) % 2 == 1) {
            return kth(nums1, nums2, m, n, (m + n + 1) / 2);
        } else {
            return (kth(nums1, nums2, m, n, (m + n) / 2) + kth(nums1, nums2, m, n, (m + n) / 2 + 1)) / 2;
        }
    }
};
```