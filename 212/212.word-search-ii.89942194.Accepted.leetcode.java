public class Solution
{
    public List<String> findWords(char[][] board, String[] words)
    {
        Set<String> result = new HashSet<String>();

        if (board == null || board.length == 0 || board[0].length == 0
            || words == null || words.length == 0)
        {
            return new ArrayList<String>(result);
        }

        boolean[][] visited = new boolean[board.length][board[0].length];
        Trie trie = new Trie(words);

        for (int i = 0; i < board.length; i++)
        {
            for (int j = 0; j < board[0].length; j++)
            {
                dfs(board, i, j, "", visited, trie, result);
            }
        }

        return new ArrayList<String>(result);
    }

    private void dfs(char[][] board, int i, int j, String str, boolean[][] visited, Trie trie, Set<String> result)
    {
        if (i < 0 || i>= board.length || j < 0 || j >= board[0].length || visited[i][j])
        {
            return;
        }

        String newStr = str + board[i][j];
        TrieNode endNode = trie.startWith(newStr);

        if (endNode == null)
        {
            return;
        }

        if (endNode.isWord == true)
        {
            result.add(newStr);
        }

        visited[i][j] = true;
        dfs(board, i + 1, j, newStr, visited, trie, result);
        dfs(board, i - 1, j, newStr, visited, trie, result);
        dfs(board, i, j + 1, newStr, visited, trie, result);
        dfs(board, i, j - 1, newStr, visited, trie, result);
        visited[i][j] = false;
    }

    class Trie
    {
        TrieNode root;

        public Trie(String[] words)
        {
            root = new TrieNode();

            for (String word : words)
            {
                insert(word);
            }
        }

        // gets the last node in the tree that matches the str, return null if not match
        public TrieNode startWith(String prefix)
        {
            TrieNode current = root;

            for (int i = 0; i < prefix.length(); i++)
            {
                TrieNode node = current.children.get(prefix.charAt(i));

                if (node == null)
                {
                    return null;
                }

                current = node;
            }

            return current;
        }

        public void insert(String word)
        {
            TrieNode current = root;

            for (int i = 0; i < word.length(); i++)
            {
                char c = word.charAt(i);
                TrieNode node = current.children.get(c);

                if (node == null)
                {
                    current.children.put(c, new TrieNode(c));
                    node = current.children.get(c);
                }

                current = node;
            }

            current.isWord = true;
        }
    }

    class TrieNode
    {
        boolean isWord;
        char content;
        Map<Character, TrieNode> children;

        public TrieNode()
        {
            this.content = ' ';
            this.isWord = false;
            this.children = new HashMap<Character, TrieNode>();
        }

        public TrieNode(char content)
        {
            this.content = content;
            this.isWord = false;
            this.children = new HashMap<Character, TrieNode>();
        }
    }
}
