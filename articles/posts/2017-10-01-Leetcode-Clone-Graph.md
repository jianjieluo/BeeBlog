@(Coding Language & Algorithm)[LeetCode]

# Leetcode-Clone Graph

> Difficulty: Medium

> Week 4

## Description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph `{0,1,2#1,2#2,2}`.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

[原题链接](https://leetcode.com/problems/clone-graph/description/)

## Personal Solution

关于图的问题我们可以从DFS或者BFS下手，这里的话只是复制一幅图，从编程的简洁性来看，使用dfs的递归算法应该最快，但是实际上过程并没有想象中那么顺利。

DFS递归复制的主要思路应该是，创建一个数据结构来记录每一个节点是否已经被访问过（是否已经被复制）。如果没有的话就new一个，更新它的`neighbors`内容并且返回，其中更新`neighbors`的同时进行递归调用`cloneNode`方法。同时，另外维护一个数据结构用来存储已经复制过的新节点。

递归结束的标志：
1. 如果传入的node为`nullptr`，则返回`nullptr`并结束。
2. 如果传入的node已经被复制过了，则返回已经被复制过的节点的指针。

那么对于两个数据结构的选取，因为题目已知label值唯一，所以一开始准备使用一个指针数组a[MAX]来存取新复制的节点，`MAX`的值足够大。然后a数组的下标表示每个node的label唯一标识一个node。数组中的元素的值为`nullptr`，则表示这个node还没有被复制过。这样的话一个数据结构就可以同时满足一开始dfs的两个要求。

但是实际上总是会出现内存分配错误，怀疑是MAX的值取得不够大，或者是用`label`作唯一标识由什么缺漏，所以暂时不考虑数组或者vector数据结构。在C++中还能表示一一对应关系的就只有map了。

那么参考上面的思路，**node还没有复制过的情况对应于在一个`map<UndirectedGraphNode *, UndirectedGraphNode *>`的结构中找不到这样的一个key值为node的元素。**其他的思路参照不变，那么递归实现就比较容易实现出来了。

```cpp
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
#include <map>
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        map<UndirectedGraphNode *, UndirectedGraphNode *> a;
        return cloneNode(node, a);
    }
    
    UndirectedGraphNode *cloneNode(UndirectedGraphNode *node, map<UndirectedGraphNode *, UndirectedGraphNode *>& a) {
        if (node == nullptr) return nullptr;
        
        if (a.end() != a.find(node)) {
            return a[node];
        }
        
        auto newnode = new UndirectedGraphNode(node->label);
        a[node] = newnode;
        
        for (auto item : node -> neighbors) {
            auto temp = cloneNode(item, a);
            if (temp != nullptr) {
                newnode->neighbors.push_back(temp);
            }
        }
        return newnode;
    }
};
```