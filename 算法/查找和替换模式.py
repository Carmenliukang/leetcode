#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/find-and-replace-pattern/description/


你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

返回 words 中与给定模式匹配的单词列表。

你可以按任何顺序返回答案。



示例：

输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。


提示：

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

"""


"""

这个确实没有想到，这个使用的是替换的方法，使用了 哈希表。

方法一：构造双射
我们可以逐个判断 words 中的每个单词 word 是否与 pattern 匹配。

根据题意，我们需要构造从字母到字母的双射，即 word 的每个字母需要映射到 pattern 的对应字母，并且 pattern 的每个字母也需要映射到 word 的对应字母。

我们可以编写一个函数 match(word,pattern)，仅当 word 中相同字母映射到 pattern 中的相同字母时返回 true。我们可以在遍历这两个字符串的同时，用一个哈希表记录 word 的每个字母 x 需要映射到 pattern 的哪个字母上，如果 x 已有映射，则需要检查对应字母是否相同。

如果 match(word,pattern) 和 match(pattern,word) 均为 true，则表示 word 与 pattern 匹配。

作者：力扣官方题解
链接：https://leetcode.cn/problems/find-and-replace-pattern/solutions/1593882/cha-zhao-he-ti-huan-mo-shi-by-leetcode-s-fyyg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

class Solution:

    def filter_words(self, w, p):
        if len(w) != len(p):
            return False
        return len(set(w)) == len(set(p)) == len(set(zip(w, p)))

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return [w for w in words if self.filter_words(w, pattern)]
