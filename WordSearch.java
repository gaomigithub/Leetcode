/**
 * Given a 2D board and a word, find if the word exists in the grid.
 *
 * The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
 * or vertically neighboring. The same letter cell may not be used more than once.
 *
 * Example:
 *
 * board =
 * [
 *   ['A','B','C','E'],
 *   ['S','F','C','S'],
 *   ['A','D','E','E']
 * ]
 *
 * Given word = "ABCCED", return true.
 * Given word = "SEE", return true.
 * Given word = "ABCB", return false.
 */


class findWordExistInBoard {
    public boolean exist(char[][] board, String word) {
        if (board == null || board[0] == null || board.length == 0 || board[0].length == 0 || word == null) return false;
        // find the first char of word in board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (word.charAt(0) == board[i][j]) {
                    if (dfs(i, j, 0, board, word )) {
                        return true;
                    }
                }

            }
        }
        return false;
    }

    public boolean dfs(int x, int y, int index, char[][] board, String word) {
        if (index == word.length()) {
            return true;
        }
        if (x < 0 || y < 0 || x >= board.length || y >= board[0].length || board[x][y] != word.charAt(index))
            return false;
        char tmp = board[x][y]; // save the point's value
        board[x][y] = '#'; // mark the point first
        boolean flag = dfs(x - 1, y, index + 1, board, word) ||
                dfs(x, y - 1, index + 1, board, word) ||
                dfs(x + 1, y, index + 1, board, word) ||
                dfs(x, y + 1, index + 1, board, word);
        board[x][y] = tmp;
        return flag;
    }
}