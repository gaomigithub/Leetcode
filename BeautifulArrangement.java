// Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

// The number at the ith position is divisible by i.
// i is divisible by the number at the ith position.
// Now given N, how many beautiful arrangements can you construct?

// Example 1:
// Input: 2
// Output: 2
// Explanation: 

// The first beautiful arrangement is [1, 2]:

// Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

// Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

// The second beautiful arrangement is [2, 1]:

// Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

// Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
// Note:
// N is a positive integer and will not exceed 15.


// 思路：
// 乍一想有很多种可能不知道怎么统计，而这恰恰就可以通过递归回溯来实现。

// 我们的思路是，从第一位到第N位，我们都要找到对应的没有放置过的数字来放，每一位都会有很多个数字可以放，而放了之后以后就不能放了，这样一直放到最后一位，如果都能放到数字，那就是一种漂亮的安排，总结果就要加一。

// 这种思路就可以通过递归来实现。每一次递归我们都判断当前位置有哪些没放过的数字可以放，对于数字有没有放过我们需要一个数字来记录。对于每个放在这一位的数字，都是一种可能性，我们要继续往后递归看能不能全部放完才能知道要不要算作一种。如果所有都放完了那就算作一种了，总结过可以加一。

// 要注意这里的位置并不是从0开始算的，而是1。

// 作者：Cloudox_
// 链接：https://www.jianshu.com/p/b9783af4b258
// 來源：简书
// 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

public class Solution {
    public int countArrangement(int N) {
        int[] num = new int[N];
        int res = findWay(num, 1);
        return res;
    }
    
    public int findWay(int[] num, int index) {
        if (index == num.length+1) return 1;
        int total = 0;
        for (int i = 0; i < num.length; i++) {
            if (num[i] != 1) {
                if ((i+1) % index == 0 || index % (i+1) == 0) {
                    int[] newNum = num.clone();
                    newNum[i] = 1;
                    total += findWay(newNum, index+1);
                }
            }
        }
        return total;
    }
}