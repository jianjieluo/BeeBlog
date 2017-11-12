@(Coding Language & Algorithm)[LeetCode]

# LeetCode-Course Schedule

> Week 10

> Difficulty: Medium

## Description

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

```
2, [[1,0]]
```
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

```
2, [[1,0],[0,1]]
```

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Note:**
1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.

[原题链接](https://leetcode.com/problems/course-schedule/description/)

## Personal Solution

此题是一个拓扑排序的问题，而且只是需要检查一个图能够进行拓扑排序，**判读一个图能否进行拓扑排序的关键是看此图是否是一个有向无环图。**而判断一张图是否是有环可以使用DFS来判断。如果从一个顶点出发，可以到达一个已经访问过的顶点，那么此图有环，也就不可以进行拓扑排序。整个过程需要用一个`visited`数组来记录各个顶点的访问情况。

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool flag;
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        // 构造对应的图
        vector<vector<bool>> edge(numCourses, vector<bool>(numCourses, false));
        for (auto item : prerequisites) {
            edge[item.second][item.first] = true;
        }

        vector<int> visited(numCourses, 0);
        
        flag = true;
        for (int i = 0; i < numCourses; ++i) {
            if (visited[i] == 0) {
                dfs(edge, visited, i, numCourses);
            }
        }
        return flag;
    }
    
    void dfs(const vector<vector<bool>>& edge, vector<int>& visited, int vex, int numCourses) {
        if (flag) {
            if (visited[vex] == -1) {
                flag = false;
            } else {
                visited[vex] = -1;
                for (int i = 0; i < numCourses; ++i) {
                    if (edge[vex][i]) {
                        dfs(edge, visited, i, numCourses);
                    }
                }
                visited[vex] = 1;
            } 
        }
    }
};
```


