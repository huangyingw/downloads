public class Solution
{
    public String removeDuplicateLetters(String s)
    {
        if (s == null || s.length() <= 1)
        {
            return s;
        }

        // Step 1: find the last index for each char
        Map<Character, Integer> lastIndexMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            lastIndexMap.put(c, i);
        }

        // Step 2: for each character, find the smallest index in the map
        // Then find out the smallest char before the index.
        StringBuilder sb = new StringBuilder();
        int start = 0;
        int end = findSmallestIndex(lastIndexMap);

        while (!lastIndexMap.isEmpty())
        {
            char curr = 'z' + 1;
            int index = 0;

            for (int i = start; i <= end; i++)
            {
                char c = s.charAt(i);

                if ((c < curr) && (lastIndexMap.containsKey(c)))
                {
                    curr = c;
                    index = i;
                }
            }

            // append result
            sb.append(curr);
            lastIndexMap.remove(curr);
            // update the start and end
            start = index + 1;
            end = findSmallestIndex(lastIndexMap);
        }

        return sb.toString();
    }

    private int findSmallestIndex(Map<Character, Integer> lastIndexMap)
    {
        int result = Integer.MAX_VALUE;

        for (int index : lastIndexMap.values())
        {
            result = Math.min(result, index);
        }

        return result;
    }
}
