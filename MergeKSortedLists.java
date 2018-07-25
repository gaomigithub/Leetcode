// Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

// Example:

// Input:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// Output: 1->1->2->3->4->4->5->6

public class Solution {
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKListsNaive(List<ListNode> lists) {
        if (lists == null || lists.size() == 0) {
            return null;
        }
        if (lists.size() == 1) {
            return lists.get(0);
        }

        int listSize = lists.size();

        ListNode base = lists.get(0);

        for (int i = 1; i < listSize; i++) {
            base = mergeTwoLists(base, lists.get(i));
        }
        return base;
    }
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
     public ListNode mergeKLists(List<ListNode> lists) {
         if (lists.size() == 0) {
             return null;
         }
         if (lists.size() == 1) {
             return lists.get(0);
         }
         if (lists.size() == 2) {
             return mergeTwoLists(lists.get(0), lists.get(1));
         }
         return mergeTwoLists(
            mergeKLists(lists.subList(0, lists.size()/2)),
            mergeKLists(lists.subList(lists.size()/2, lists.size()))
         );
     }
}