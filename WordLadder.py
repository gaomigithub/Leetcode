# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# 此题是参考了 《南郭子綦》 的思路。 

#     解题思路：这道题使用bfs来解决。参考：http://chaoren.is-programmer.com/posts/43039.html 使用BFS, 单词和length一块记录, dict中每个单词只能用一次, 所以用过即删。
#     dict给的是set类型, 检查一个单词在不在其中(word in dict)为O(1)时间。设单词长度为L, dict里有N个单词, 
#     每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母, 看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。

# 采用了bfs的方式，每次改变单词中的一个字符，并判断生成的单词是否在wordlist中，直到生成目标单词，或者无法再继续下去。

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList) #avoid TLE
        q = [(beginWord,1)]
        while q:
            word, lens = q.pop(0)
            if word = endWord:
                return lens
            
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    nextWord = left + c + right
                    if nextWord in wordList:
                        q.append(nextWord,lens + 1)
                        wordList.remove(nextWord)
        return 0

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

# 类型：BFS
# Time Complexity O(n26^len) -> O(n26^len/2)
# Space Complexity O(n)

# 每次只要对word里面任意字母进行更改以后，就将其放回queue里面。
# 对于是否访问这个问题，我的写法是写一个visted的set来统计，LC里面有一种直接删除wordList里面访问过的词，想法雷同。
# 至于记录深度，可以利用python里面tuple的小技巧，每次迭代的时候对tuple里面的计量单位增值即可:
# q.append((new_word, length + 1))
# 最后一点就是开头的arr = set(arr) 用来解决TLE，LC里面有些特别大的重复List很尴尬。
class Solution(object):
    def ladderLength(self, start, end, arr):
        arr = set(arr) #avoid TLE
        q = collections.deque([(start, 1)])
        visted = set()
        alpha = string.ascii_lowercase  #'abcd...z'
        while q:
            word, length = q.popleft()
            if word == end:
                return length
            
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in arr and new_word not in visted:
                        q.append((new_word, length + 1))
                        visted.add(new_word)
        return 0