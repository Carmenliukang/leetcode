# [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/description/?envType=daily-question&envId=2025-02-08)

## Desc

给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]
）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 2 * 109。

示例 1：

![](https://raw.githubusercontent.com/Carmenliukang/leetcode/master/images/unique-paths-ii-1.png)

```
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

```

示例 2：

![](https://raw.githubusercontent.com/Carmenliukang/leetcode/master/images/unique-paths-ii-2.png)

![](https://raw.githubusercontent.com/Carmenliukang/leetcode/master/images/unique-paths-ii-2.png)

```
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 
```

提示：

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` 为 `0` 或 `1`

## Solution

这个是一种基本的 DP 问题，因为这个只能向右/向下 行走，所以当前的节点，只会与 它的位置的左边还有上面有关系。

```
dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] != 1 else 0
```

### Code

```python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for j in range(n)] for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            else:
                dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

```