class TrieNode
{
  boolean isWord;
  char content;
  HashMap<Character, TrieNode> nexts;

  public TrieNode()
  {
    this.content = ' ';
    this.isWord = false;
    this.nexts = new HashMap<Character, TrieNode>();
  }

  public TrieNode(char content)
  {
    this.content = content;
    this.isWord = false;
    nexts = new HashMap<Character, TrieNode>();
  }
}

public class WordDictionary
{
  private TrieNode root;

  public WordDictionary()
  {
    root = new TrieNode();
  }

  // Adds a word into the data structure.
  public void addWord(String word)
  {
    TrieNode current = root;

    for (int i = 0; i < word.length(); i++)
    {
      char c = word.charAt(i);
      TrieNode node = current.nexts.get(c);

      if (node == null)
      {
        current.nexts.put(c, new TrieNode(c));
        node = current.nexts.get(c);
      }

      current = node;
    }

    current.isWord = true;
  }

  // Returns if the word is in the data structure. A word could
  // contain the dot character '.' to represent any one letter.
  public boolean search(String word)
  {
    if (word == null || word.length() == 0)
    {
      return false;
    }

    TrieNode trieNode = root;
    return dfs(word, 0, trieNode);
  }

  private boolean dfs(String word, int index, TrieNode trieNode)
  {
    if (index == word.length() - 1)
    {
      if (word.charAt(index) == '.')
      {
        for (TrieNode tNode : trieNode.nexts.values())
        {
          if (tNode.isWord)
          {
            return true;
          }
        }

        return false;
      }
      else
      {
        TrieNode endNode = trieNode.nexts.get(word.charAt(index));
        return endNode != null && endNode.isWord;
      }
    }

    if (index >= word.length())
    {
      return false;
    }

    if (word.charAt(index) == '.')
    {
      for (TrieNode node : trieNode.nexts.values())
      {
        if (dfs(word, index + 1, node))
        {
          return true;
        }
      }

      return false;
    }
    else
    {
      if (trieNode.nexts.containsKey(word.charAt(index)))
      {
        return dfs(word, index + 1, trieNode.nexts.get(word.charAt(index)));
      }
      else
      {
        return false;
      }
    }
  }
}

