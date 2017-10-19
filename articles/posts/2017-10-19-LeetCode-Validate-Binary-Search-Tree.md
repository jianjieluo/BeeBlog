@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Validate Binary Search Tree

> Difficulty: Medium

> Week 7

## Description

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
```
    2
   / \
  1   3
```
Binary tree [2,1,3], return true.
Example 2:
```
    1
   / \
  2   3
```
Binary tree [1,2,3], return false.

[原题链接](https://leetcode.com/problems/validate-binary-search-tree/description/)

## Personal Solution

二叉搜索树一个重要的性质就是它的中序遍历是一个有序数列，那么我脑海中的第一反应是直接进行一次中序遍历并把结果存进一个数组a中，然后检测a是否是一个有序数列即可。

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
#define MAX 10000
class Solution {
public:
    int content[MAX];
    int count;
    
    void inorder(TreeNode* root) {
        if (root == nullptr) return;
        
        inorder(root->left);
        content[count++] = root->val;
        inorder(root->right);
    }
    
    bool isValidBST(TreeNode* root) {
        for (int i = 0; i < MAX; ++i) {
            content[i] = 0;
        }
        count = 0;
        
        inorder(root);
        
        for (int i = 0 ; i < count; ++i) {
            for (int j = count-1; j > i; --j) {
                if (content[j] <= content[i]) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

成功AC，但是运行的速度不敢恭维，只有122ms，在leetcode上的统计记录中排在很后的位置，细想一下这个朴素的算法就可以知道有很大的一部分开销是用在了判断有序数列的操作上，思考优化后的方案，可以知道其实没有必要进行两层嵌套循环，只要进行一次循环，每次判断`a[i]`和`a[i+1]`的值的相对大小就可以知道该序列是否是有序数列了。将上述代码中的

```cpp
for (int i = 0 ; i < count; ++i) {
    for (int j = count-1; j > i; --j) {
        if (content[j] <= content[i]) {
            return false;
        }
    }
}
```

修改为：

```cpp
for (int i = 0; i < count-1; ++i) {
    if (content[i] >= content[i+1]) {
        return false;
    }
}
```

即得到了优化版本，运行速度从122ms提升到了13ms左右。


## An Alternative Solution Using Recursion

上述的解法开了全局大数组来存储中序遍历的结果，如果实际情况下对于空间的开销有限制的话，有另外一种递归解法的思路。递归的思路是：根节点的右子树的所有节点值都要比根节点的大，根节点的左子树的所有节点值都要比根节点小。递归写法不难思考，需要注意的是函数声明的形参的数据类型要开大一点，不能仅仅用`int`。

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
#include <climits>
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, LLONG_MIN, LLONG_MAX);
    }
    
    bool isValidBST(TreeNode* root, long long int min, long long int max) {
        if (root == nullptr) return true;
        
        if ((root->val < max) && (root->val > min) && 
            isValidBST(root->left, min, root->val) &&
           isValidBST(root->right, root->val, max)) {
            return true;
        } else {
            return false;
        }
    }
};
```

运行速度是13ms左右，和第一种解法不差上下，但是大大地减少了空间上的开销。仅仅用dfs结合递归就实现了需求。