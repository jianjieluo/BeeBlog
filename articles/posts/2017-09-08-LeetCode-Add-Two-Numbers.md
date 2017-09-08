# Add Two Numbers

@(Coding Language & Algorithm)[LeetCode]


> Difficulty: Medium

## Description	
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Input:** (2 -> 4 -> 3) + (5 -> 6 -> 4)
**Output:** 7 -> 0 -> 8

[原题链接](https://leetcode.com/problems/add-two-numbers/description/)


## Personal Solution

此题仅仅从算法上面分析没有特别有难度的地方，直接使用朴素的算法遍历两个列表就可以解决问题，容易忽略和出错的一些问题是：

1.  两个列表之间可以相加的条件。
2.  最高位进位的话应该需要把进位再增加到队列尾部。
3.  每一次迭代加法的过程中列表指针和进位的变化。
4.  迭代过程边界条件的思考。


### First AC Version

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = nullptr;
        ListNode* tail = nullptr;
        int jinwei = 0;
        while (!(l1 == nullptr && l2 == nullptr)) {
            auto a = (l1 == nullptr) ? 0 : l1->val;
            auto b = (l2 == nullptr) ? 0 : l2->val;
            
            ListNode* resNode = new ListNode((a+b+jinwei)%10);
            jinwei = (a+b+jinwei) / 10;
            
            if (res == nullptr) {
                res = resNode;
            } else {
                tail->next = resNode;
            }
            tail = resNode;
            
            l1 = (l1 == nullptr) ? nullptr : l1->next;
            l2 = (l2 == nullptr) ? nullptr : l2->next;
        }
        
        if (jinwei != 0) {
            ListNode* resNode = new ListNode(1);
            tail->next = resNode;
        }
        
        return res;
    }
};
```