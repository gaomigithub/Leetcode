// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

// Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

// Example 2: Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

// This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

// 排序法
// 复杂度
// 时间 O(NlogN) 空间 O(N)

// 思路
// 和Merge Interval的思路接近，这题中我们只有一个待合并的Interval，就是输入给出的。
// 我们只要把所有和该Interval有重叠的合并到一起就行了。
// 为了方便操作，对于那些没有重叠部分的Interval，我们可以把在待合并Interval之前的Interval加入一个列表中，
// 把之后的Interval加入另一个列表中。最后把前半部分的列表，合并后的大Interval和后半部分的列表连起来，就是结果了。

// 注意
// 1. 因为待合并的Interval出现的位置不确定，判断重叠与否时既要判断起点，也要判断终点
// 2. 原列表为空时，直接加入待合并的Interval后返回

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> before = new LinkedList<Interval>();
        List<Interval> after = new LinkedList<Interval>();
        List<Interval> res = new LinkedList<Interval>();
        if(intervals.size() == 0){
            res.add(newInterval);
            return res;
        }
        // 排序
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval i1, Interval i2){
                return i1.start - i2.start;
            }
        });
        for(Interval itx : intervals){
            // 将待合并Interval之前的存入一个列表中
            if(newInterval.start > itx.end){
                before.add(itx);
            }
            // 将有重叠的Interval都合并起来
            if((newInterval.end >= itx.start && newInterval.end <= itx.end) || (newInterval.start <= itx.end && newInterval.start >= itx.start)){
                newInterval.start = Math.min(newInterval.start, itx.start);
                newInterval.end = Math.max(newInterval.end, itx.end);
            }
            // 将待合并Interval之后的存入一个列表中
            if(newInterval.end < itx.start){
                after.add(itx);
            }
        }
        // 把三部分加起来
        res.addAll(before);
        res.add(newInterval);
        res.addAll(after);
        return res;
    }
}