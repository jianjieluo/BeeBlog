@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Maximum Depth of Binary Tree

> Difficulty: Easy

> Week 6

## Description
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

[原题链接](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

## Personal Solution

寻找一棵二叉树的最大深度，使用一次dfs即可，使用全局变量`max`来记录最大深度，并且在dfs的每次遍历中带上当前节点所在的层数信息。

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
    int max;
    
    int maxDepth(TreeNode* root) {
        max = 0;
        dfs(root, 1);
        return max;
    }
    
    void dfs(TreeNode* root, int currlevel) {
        if (root == nullptr) return; 
        if (max < currlevel) {
            max = currlevel;
        }
        if (root->left != nullptr) {
            dfs(root->left, currlevel+1);
        }
        if (root->right != nullptr) {
            dfs(root->right, currlevel+1);
        }
    }
};
```