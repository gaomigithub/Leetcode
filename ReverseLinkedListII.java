/**
 * Reverse a linked list from position m to n. Do it in one-pass.
 *
 * Note: 1 ≤ m ≤ n ≤ length of list.
 *
 * Example:
 *
 * Input: 1->2->3->4->5->NULL, m = 2, n = 4
 * Output: 1->4->3->2->5->NULL
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class RevLinkedListMToNOnePass {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode mNode = head;
        ListNode preM = dummy;
        ListNode nNode = head;
        for (int i = 1; i < m; i++) {
            preM = mNode;
            mNode = mNode.next;
        }
        for (int i = 1; i < n; i++) {
            nNode = nNode.next;
        }
        while (mNode != nNode) {
            preM.next = mNode.next;
            mNode.next = nNode.next;
            nNode.next = mNode;
            mNode = preM.next;
        }
        return dummy.next;
    }
}