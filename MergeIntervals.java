// Given a collection of intervals, merge all overlapping intervals.

// For example, Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].

// 排序法
// 复杂度
// 时间 O(NlogN) 空间 O(N)

// 思路
// 首先根据Interval的起点，我们将其排序，这样能合并的Interval就一定是相邻的了：

// [1,3] [5,6] [2,3]
// ---> [1,3] [2,3] [5,6]
// 然后我们就顺序遍历这个列表，并记录一个当前待合并的Interval，
// 如果遍历到的Interval和当前待合并的Interval有重复部分，我们就将两个合并，
// 如果没有重复部分，就将待合并的Interval加入结果中，并用新的Interval更新这个待合并的Interval。
// 因为数组已经排过序，前面的Interval的起点肯定小于后面Interval的起点，
// 所以在判断是否有重叠部分时，只要考虑待合并的Interval的终点和遍历到的Interval的起点的关系就行了。

// 注意
// 1. 判断重叠的边界时包含等于的情况
// 2. 循环后还要把最后一个待合并的Interval也加入结果中
// 3. 更新待合并Interval的边界时，要同时更新起点和终点

public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> res = new LinkedList<Interval>();
        if(intervals.size() == 0){
            return res;
        }
        // 按照起点排序
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval i1, Interval i2){
                return i1.start - i2.start;
            }
        });
        // 拿出第一个待合并的Interval
        Interval curr = intervals.get(0);
        for(Interval itv : intervals){
            // 如果有重叠部分，更新待合并的Interval的起点和终点
            if(curr.end >= itv.start){
                curr.start = Math.min(curr.start, itv.start);
                curr.end = Math.max(curr.end, itv.end);
            } else {
            // 否则将待合并的Interval加入结果中，并选取新的待合并Interval
                res.add(curr);
                curr = itv;
            }
        }
        // 将最后一个待合并的加进结果
        res.add(curr);
        return res;
    }
}
