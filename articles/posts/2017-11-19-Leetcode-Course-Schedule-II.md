@(Coding Language & Algorithm)[LeetCode]

# Leetcode-Course Schedule II

> Difficulty:  Medium

> Week:  11

## Description

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

```
2, [[1,0]]
```

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

```
4, [[1,0],[2,0],[3,1],[3,2]]
```

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is `[0,1,2,3]`. Another correct ordering is`[0,2,1,3]`.

[原题链接](https://leetcode.com/problems/course-schedule-ii/description/)

## Personal  Solution

这一题是一道拓扑排序的问题，一张图可以进行拓扑排序的前提是**该图需要是有向无环图**，在满足了这个的前提下， 根据《算法概论》中对于图的dfs遍历的`pre`值和`post`值的定义：

```
procedure previsit(v):
pre[v] = clock
clock = clock + 1

procedure postvisit(v):
post[v] = clock
clock = clock + 1
```

当进行完了整个dfs遍历后，将每个节点按照其post值从大到小地进行输出，输出的结果就是一个拓扑排序的结果了。

在[LeetCode Course Schedule](https://longjj.com/2017/11/12/LeetCode-Course-Schedule/)这个解答的基础上，在dfs判断是否可以进行拓扑排序的同时附加上post值的信息，那么就可以得到拓扑排序了。

## First AC Version

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int clock;
    
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<bool>> edge(numCourses, vector<bool>(numCourses, false));
        for (auto item : prerequisites) {
            edge[item.second][item.first] = true;
        }
        vector<int> visited(numCourses, 0);
        vector<int> post(numCourses, 0);
        
        clock = 1;
        
        vector<int> ret;
        ret.clear();
        
        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(edge, visited, post, numCourses, i)) {
                return ret;
            }
        }
        
        int a[numCourses+1];
        for (int i = 0; i < numCourses; ++i) {
            a[post[i]] = i;
        }
        for (int i = numCourses; i > 0; --i) {
            ret.push_back(a[i]);
        }
        return ret;
    }
    
    bool dfs(const vector<vector<bool>>& edge, vector<int>& visited, vector<int>& post, int numCourses, int i) {
        if (visited[i] == -1) return false;
        if (visited[i] == 1) return true;
        visited[i] = -1;
        for (int j = 0; j < numCourses; ++j) {
            if (edge[i][j]) {
                if (!dfs(edge, visited, post, numCourses, j)) return false;
            }
        }
        visited[i] = 1;
        post[i] = clock++;
        return true;
    }
};
```