@(Coding Language & Algorithm)[LeetCode]

[TOC]

# LeetCode-Unique Binary Search Trees II

> Difficulty: Medium
>
> Week 15

## Description

（原题95）

Given an integer *n*, generate all structurally unique **BST's** (binary search trees) that store values 1...*n*.

For example,
Given *n* = 3, your program should return all 5 unique BST's shown below.

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

[原题链接](https://leetcode.com/problems/unique-binary-search-trees-ii/description/)

## Personal Solution

构造树的题目一般都是用递归构造。因为已经做过了Unique Binary Search Trees这道题目，所以思路上可以有所借鉴。此题在写的时候逻辑关系非常容易搞乱，鄙人在这里使用了简单粗暴地返回`vector`。每一次递归迭代拿到了该层的左右子树的各种组合之后，需要一个一个地拼接起来形成该层的BST树的所有结果。



总体来说使用的是递归的暴力解法，每次递归，3层for循环，最外层取一个数为root，然后递归get到左右子树的所有组成lchild和rchild，然后里面的两层循环遍历left和right的所有组合和root组成一个新的树，加入ret的这个vector中。

### First AC Version

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
    vector<TreeNode*> generateTrees(int n) {
        if (n < 1) {
            vector<TreeNode*> res;
            res.clear();
            return res;
        }
        auto res = gen(1, n);
        return res;
    }
    
    vector<TreeNode*> gen(const int lsh, const int rsh) {
        vector<TreeNode*> ret;
        ret.clear();
        
        if (lsh > rsh) {
            ret.push_back(nullptr);
            return ret;
        }
        
        if (lsh == rsh) {
            ret.push_back(new TreeNode(lsh));
            return ret;
        }
        
        for (int i = lsh; i < rsh+1; ++i) {
            // xuan zi root
            auto leftset = gen(lsh, i-1);
            auto rightset = gen(i+1, rsh);
            
            // 暴力枚举所有可能，并加入ret中
            for (int l = 0; l < leftset.size(); ++l) {
                for (int r = 0; r < rightset.size(); ++r) {
                    TreeNode* root = new TreeNode(i);
                    root->left = leftset[l];
                    root->right = rightset[r];
                    ret.push_back(root);
                }
            }
        }
        return ret;
    }
};
```