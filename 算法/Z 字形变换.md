
# [Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)


## Desc

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：
```
P   A   H   N
A P L S I I G
Y   I   R

```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：
```
string convert(string s, int numRows);
 
```
示例 1：
```
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

```

示例 2：
```
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

```

示例 3：
```
输入：s = "A", numRows = 1
输出："A"
 
```
提示：

- `1 <= s.length <= 1000`
- `s` 由`英文字母（小写和大写）`、`','` 和 `'.'` 组成
- `1 <= numRows <= 1000`

## Code

这个Z变换需要注意的是确定 变换的方向，具体是向上还是向下。需要一个参数 mark 标识，
变换的条件是: row 到最大值，或者 row 变成最小。

```python

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        result = [[] for i in range(numRows)]
        row = -1
        # mark 代表的是 向上还是向下
        mark = True
        for i in s:

            if mark is True:
                row += 1
                if row == numRows-1:
                    mark = False
            else:
                row -= 1
                if row == 0:
                    mark = True
            result[row].append(i)
        
        return "".join(["".join(i) for i in result])
```