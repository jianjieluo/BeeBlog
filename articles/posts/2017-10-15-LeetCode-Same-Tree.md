@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Same Tree

> Difficulty: Easy

> Week 6

## Description

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

[原题链接](https://leetcode.com/problems/same-tree/description/)

## Personal Solution

本题主要考察的是二叉树的dfs，在dfs的基础上做一些变化即可。在这题里面，只要同时对两棵树进行dfs遍历，并且判读当前点是否一样即可。使用递归写法来简化代码，使用全局变量`isSame`来加速算法，当当前的`isSame`值为false的时候就不再进入dfs的判断过程。

在当前节点的判断分类：
1. p,q 均为nullptr，直接return。
2. p,q 有一个为空另一个不为空，将`isSame`设为false并return
3. p,q 均不为空但对应的值不相等，将`isSame`设为false并return
4. 分别递归判读p,q 的左右子树。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSame;
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        isSame = true;
        doubledfs(p, q);
        return isSame;
    }
    
    void doubledfs(TreeNode* p, TreeNode* q) {
        if (isSame) {
            if (p == nullptr && q == nullptr) return;
            if (p != nullptr && q == nullptr) {
                isSame = false;
                return;
            }
            if (p == nullptr && q != nullptr) {
                isSame = false;
                return;
            }
            
            if (p->val != q->val) {
                isSame = false;
                return;
            }
            
            doubledfs(p->left, q->left);
            doubledfs(p->right, q->right);
        }
    }
};
```