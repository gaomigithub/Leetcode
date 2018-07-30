# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# 1.我们把起始字符串当成根节点，如果在变化过程中，某一个节点是目标字符串，那么就找到了一条变化路径。
# 2.节点所在的高度能够反映出变化到该节点时经历了几次变化，如hot在根节点的下一层，表示变化了一次，hut和bot在更下一层，表示变化了两次。
# 3.在树上层出现过的字符串没必要在下层再次出现，因为如果该字符串是转换过程中必须经过的中间字符串，那么应该挑选上层的该字符串继续进行变化，它的转换次数少。
# 4.如果上一层有多个字符串可以转换为下一层同一个字符串，那么只需要找到其中一个转换关系即可，如例子中的bit和him都可以转为bim，我们只需要知道有一条关系可以走到bim就可以了，没必要找到所有的转换关系，因为这样已经可以确定进行两次转换就能变为bim。
# 5.基于第3和第4点，当集合中的字符串在树中出现后，就可以把它从集合中删除。这样可以防止字符串不断地循环转化。
# 6.至此，这个问题就变为一个深度优先遍历(DFS)问题，只需要依次遍历每一层的节点，如果在该层找到了目标字符串，只要返回相应的变化次数。如果到某一层树的节点无法继续向下延伸，且没有找到目标字符串，那么就是不存在这样的转换关系，返回0

# For example:
#         hit
#       / / \ \
#     /  /   \  \
#  hot  hat  bit him
#            /  \ |
#          bot    bim

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        cur_level = [beginWord]
        next_level = []
        depth = 1
        n = len(beginWord)
        while cur_level:
            for item in cur_level:
                if item == endWord:
                    return depth
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word = item[:i] + c + item[i + 1:]
                        if word in wordList:
                            wordList.remove(word)
                            next_level.append(word)
            depth += 1
            cur_level = next_level
            next_level = []
        return 0