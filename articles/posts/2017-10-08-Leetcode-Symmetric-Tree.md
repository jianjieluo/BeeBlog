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

此题有递归解法和非递归解法两种方法。

###  递归解法
递归的算法比较容易想到，对于一个节点，只要它左右都是对称的，那么这棵树就是对称的。

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

### 非递归解法

关于对称，初始想法是使用bfs来遍历一次每一层，然后用栈来判读每一层是否对称即可。

实际实现起来并不是那么简单。我的初始想法是bfs把结果存在一个一维数组中，然后一层一层地读，每一层的情况用栈去检查对称。实际的难点在于如何正确地知道每一层有多少个节点。这里就有一点特例的方法了，并不具有普适性。我对于空节点的处理方法是bfs时检查到nullptr后就不加入队列。这样的话bfs后如果有两层以上有nullptr存在的话，在我的结果数组中每一层应该访问的节点数将不是简单的$2 ^ currlevel$个，而是会丢失部分nullptr。经过思考后我想出了这样一个方法，给多一个全局变量currnullnums，它表示当前检查到的`nullptr`的数目，那么在每一层访问的数量就应该是`auto num = pow(2, i-1) - currnullnums * 2`（因为上层的每一个nullptr都会对下层的节点个数产生影响）。然后在整个过程中维护好`currnullnums`即可。

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
#include <queue>
#include <vector>
#include <stack>
#include <math.h>

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int count = 0;
        
        int currnullnums = 0;
        vector<TreeNode*> v;
        
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            
            v.push_back(curr);
            ++count;
            
            if (curr == nullptr) continue;
            
            q.push(curr->left);
            q.push(curr->right);
        }
        
        int index = 1;
        // 假设题目中的树的层数不超过100
        for (int i = 1; i < 100; ++i) {
            if (index >= count) break;
            
            stack<TreeNode*> s;
            
            currnullnums *= 2;
            auto num = pow(2, i-1) - currnullnums;

            for (int j = 0; j < num; ++j) {
                s.push(v[index++]);
            }

            for (int j = 0; j < num; ++j) {
                auto temp = v[index++];
                if (temp == nullptr && s.top() == nullptr) {
                    s.pop();
                    currnullnums += 1;
                } else if (temp != nullptr && s.top() != nullptr) {
                    if (temp->val == s.top()->val) {
                        s.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};
```