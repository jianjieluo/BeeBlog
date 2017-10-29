@(Coding Language & Algorithm)[LeetCode]

# Leetcode-Recover Binary Search Tree

> Difficulty: Hard

> Week 8

## Description

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

[原题链接](https://leetcode.com/problems/recover-binary-search-tree/description/)

## Personal Solution

从朴素算法来思考的话，此题并不算难，因为**BST的中序遍历是一个有序的数组**，所以可以通过这样暴力求解：先进行一次中序遍历，将结果存在一个数组中，然后对数组进行排序，再进行一次中序遍历，将排序后的数组一个一个地赋值给树的节点。

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
#include <algorithm>
#define MAX 1000

class Solution {
public:
    int nodenum;
    int ret[MAX];
    
    void recoverTree(TreeNode* root) {
        for (int i = 0; i < MAX; ++i) {
            ret[i] = 0;
        }
        nodenum = 0;
        
        inorderGet(root);
        std::sort(ret, ret + nodenum);
        nodenum = 0;
        inorderSet(root);
    }
    
    void inorderGet(TreeNode* root) {
        if (root == nullptr) return;
        
        inorderGet(root->left);
        ret[nodenum++] = root->val;
        inorderGet(root->right);
    }
    
    void inorderSet(TreeNode* root) {
        if (root == nullptr) return;
        
        inorderSet(root->left);
        root->val = ret[nodenum++];
        inorderSet(root->right);
    }
};
```

实际上这样做，并没有限制说BST只有两个数交换了位置，而是无论顺序如何混乱都可以纠正过来，并且有一个大的数组开销去缓存中序遍历的结果。题目有一个bonus让你去思考如何使用o(1)的空间开销的解法。经过查找资料，了解了一种`Morris Inorder Tree Traversal`的遍历方法。

### Morris Inorder Tree Traversal

[参考视频(youtube)](https://www.youtube.com/watch?v=wGXB9OWhPTg)

我们要明白，遍历一棵树，主要是要保留子节点到父节点的联系，这样子才能够当访问完子节点后能够回来继续访问父节点。**在非递归的遍历实现中一般算法是手动维护一个栈，在递归实现中栈交给操作系统的函数栈来实现。**而`Morris Inorder Tree Traversal`使用了另外一种思路去建立父子节点的联系。为此它引入了一个`predecessor`的概念，**一个node的predecessor是它的左儿子的最右的右儿子**，例如

```
          1
        /   \
       2     3
     /   \
   4       5  
          / \
        6    7
```

上面这棵树，节点1的`predecessor`为节点7。Morris算法的核心是**通过`predeccessor`的right来和父节点建立联系**

算法的伪代码如下：

```
curr = root
while curr is not null:
	if not exists curr.left:
		visit(curr)
		curr = curr.right
	else:
		predecessor = findPredecessor(curr)
		if not exists predecessor.right:
			predecessor.right = curr
			curr = curr.left
		else:
			predecessor.right = null
			visit(curr)
			curr = curr.right
```

如何找到两个位置错误的节点呢？我们可以使用3个指针，在模拟中序遍历的过程中，pre代表前一个访问的节点，那么我们每次访问节点的时候看一下pre的值是否比curr的值要大，如果是的话就会发现问题了。当我们第一次发现问题的时候，pre所指的节点是有问题的，我们存为p1；接下来因为p1的改变影响到了后面的情况，所以我们要不断更新另一个指针p2，让p2的值保持为最新的出现问题的curr，那么最后只要交换p1p2两个指针的值即可。

### Second AC Version

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

#include <iostream>

class Solution {
public:
    
    TreeNode* pre;
    TreeNode* p1;
    TreeNode* p2;
    
    void recoverTree(TreeNode* root) {
        pre = nullptr;
        p1 = nullptr;
        p2 = nullptr;
        
        TreeNode* curr = root;
        while (curr != nullptr) {
            if (curr->left == nullptr) {
                visit(curr);
                curr = curr->right;
            } else {
                auto predecessor = findPredecessor(curr);
                if (predecessor->right == nullptr) {
//                  建立起到上一层的链接
                    predecessor->right = curr;
                    curr = curr->left;
                } else {
//                  清空已经访问过的回路
                    predecessor->right = nullptr;
                    visit(curr);
                    curr=curr->right;
                }
            }
        }

        auto temp = p1->val;
        p1->val = p2->val;
        p2->val = temp;
    }
    
    void visit(TreeNode* curr) {
        if (pre == nullptr) {
            pre = curr;
        } else {
            if (pre->val > curr->val) {
                if (!p1) p1 = pre;
                p2 = curr;
            }
            pre = curr;
        }
    }
    
    TreeNode* findPredecessor(TreeNode* curr) {
        auto ret = curr->left;
        while (ret->right != nullptr && ret->right != curr)
            ret = ret->right;
        return ret;
    }
};
```