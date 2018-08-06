// Given a collection of distinct integers, return all possible permutations.

// Example:

// Input: [1,2,3]
// Output:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]

// 思路：
// 这就是中学时排列组合的题目，要极尽所有排列，我们就要从第一个位置开始所有的元素都有可能放一遍，第二个位置在放了第一个位置的数字后剩下的数字又都可能放一遍，第三个位置也是类似，一直到最后一个位置。

// 对于这种操作用递归最合适，在我们创建的函数中对于第i个位置，每个当前还剩下的数字都去尝试放一次，并且继续往下递归，最后就会得到所有可能的排列。

// 要注意的一点就是在递归中我们的List和数组都要进行深拷贝然后添加元素，否则不同的放置方式操作的都是同一个List或者数组，没有意义。

public class Solution {
  public List<List<Integer>> permute(int[] nums) {
      List<List<Integer>> resList = new ArrayList<List<Integer>>();
      for (int i = 0; i < nums.length; i++) {
          List<Integer> list = new ArrayList<Integer>();
          list.add(nums[i]);
          int[] hasUsed = new int[nums.length];
          hasUsed[i] = 1;
          doPermute(nums, resList, list, hasUsed);
      }
      return resList;
  }
  
  public void doPermute(int[] nums, List<List<Integer>> resList, List<Integer> list, int[] hasUsed) {
      if (list.size() == nums.length) {
          resList.add(list);
          return;
      }
      for (int i = 0; i < nums.length; i++) {
          if (hasUsed[i] == 0) {
              List<Integer> newList = new ArrayList<Integer>();
              newList.addAll(list);
              newList.add(nums[i]);
              int[] newUsed = hasUsed.clone();
              newUsed[i] = 1;
              doPermute(nums, resList, newList, newUsed);
          }
      }
  }
}