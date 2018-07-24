/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 *
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 *
 * Example:
 *
 * Given nums = [2, 7, 11, 15], target = 9,
 *
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 */

import java.util.HashMap;

/**
 * Time & Space complex: O(n)
 */

public class TwoSum {
    class twoSum {
        public int[] twoSum(int[] nums, int target) {
            int[] res = new int[2];
            if (nums == null || nums.length <= 1) return res;
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            for (int i = 0; i < nums.length; i++) {
                int num = nums[i];
                int val = target - num;
                if (map.containsKey(val)) {
                    res[0] = i;
                    res[1] = map.get(val);
                    return res;
                } else map.put(num, i);
            }
            return res;
        }
    }

}
