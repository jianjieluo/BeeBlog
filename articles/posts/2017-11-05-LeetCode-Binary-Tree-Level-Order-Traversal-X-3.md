@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Binary Tree Level Order Traversal X 3

> Difficulty: Medium

> Week: 9

## Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
```
[
  [3],
  [9,20],
  [15,7]
]
```
[原题链接](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

## Personal Solution

二叉树层次遍历的问题，层次遍历使用BFS就可以完成，需要另外构建一个struct记录下每一个节点的层数的信息，然后根据各自的层数放进合适的vector中即可。

```cpp
#include <queue>
using namespace std;

class Solution {
public:
    
    struct node {
        TreeNode* ptr;
        int level;
        
        node(TreeNode* p, int l) : ptr(p), level(l) {}
    };
    
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        if (root == nullptr) {
            ret.clear();
            return ret;
        }
        
        queue<node> q;
        q.push(node(root, 1));
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            
            if (curr.level == ret.size()+1) {
                vector<int> temp{curr.ptr->val};
                ret.push_back(temp);
            } else if (curr.level == ret.size()) {
                ret.back().push_back(curr.ptr->val);
            }
            
            if (curr.ptr->left != nullptr) {
                q.push(node(curr.ptr->left, curr.level+1));
            }
            if (curr.ptr->right != nullptr) {
                q.push(node(curr.ptr->right, curr.level+1));
            }      
        }
        return ret;
    }
};
```

另外，Leetcode上还有另外两道题目与此题非常相似，主要是在遍历后得到的结果再作二次处理即可。

1. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)
此题只需要把偶数层的vector反转一下即可。
2. [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)
此题只需要把表示每一层的vector掉转即可。