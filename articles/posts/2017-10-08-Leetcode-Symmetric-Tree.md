@(Coding Language & Algorithm)[LeetCode]

# Leetcode-Symmetric Tree

> Difficulty: Easy

> Week 5

## Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
But the following `[1,2,2,null,3,null,3]` is not:
```
    1
   / \
  2   2
   \   \
   3    3
```

[原题链接](https://leetcode.com/problems/symmetric-tree/description/)

## Personal Solution

此题有递归解法和非递归解法两种方法。非递归算法想了挺久还是暂时没有能够想出来，主要是卡在了对于每一层的空指针的判定上，所以今天的post先给出递归的算法。

递归的算法就比较容易想到了，对于一个节点，只要它左右都是对称的，那么这棵树就是对称的。

递归结束的简单条件是：
1. 左右子节点只要有一个是空指针就可以结束了
	2. 如果l和r都空，则真
	3. 如果l和r只有一个为空，则假
	4. 否则进入下一阶段的判断
2. l， r两个都不空，如果两个的值不一样，则假
3. 递归迭代，左儿子的左子树和右儿子的右子树应该对称；左儿子的右子树和右儿子的左子树应该对称。
4. 如果上述情况都没有出现false，则返回true

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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        
        return isSymmertic_re(root->left, root->right);
    }
    
    bool isSymmertic_re(TreeNode* l, TreeNode* r) {
        if (l == nullptr && r != nullptr) return false;
        if (l != nullptr && r == nullptr) return false;
        if (l == nullptr && r == nullptr) return true;
        if (l->val != r->val) return false;
        
        if (!isSymmertic_re(l->left, r->right)) return false;
        if (!isSymmertic_re(l->right, r->left)) return false;
        
        return true;
    }
};
```
