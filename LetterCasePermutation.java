// Solution 1: DFS

// Time complexity: O(n*2^l), l = # of letters in the string

// Space complexity: O(n) + O(n*2^l)

// Author: Huahua
// Running time: 8 ms
class Solution {
    public List<String> letterCasePermutation(String S) {
      List<String> ans = new ArrayList<>();
      dfs(S.toCharArray(), 0, ans);
      return ans;
    }
    
    private void dfs(char[] S, int i, List<String> ans) {
      if (i == S.length) {
        ans.add(new String(S));
        return;
      }    
      dfs(S, i + 1, ans);    
      if (!Character.isLetter(S[i])) return;
      S[i] ^= 1 << 5;
      dfs(S, i + 1, ans);
      S[i] ^= 1 << 5;
    }
  }