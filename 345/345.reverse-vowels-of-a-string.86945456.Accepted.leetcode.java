public class Solution
{
    public String reverseVowels(String s)
    {
        Set<Character> vowList = new HashSet<Character>();
        vowList.add('a');
        vowList.add('e');
        vowList.add('i');
        vowList.add('o');
        vowList.add('u');
        vowList.add('A');
        vowList.add('E');
        vowList.add('I');
        vowList.add('O');
        vowList.add('U');
        char[] arr = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;

        while (left < right)
        {
            if (!vowList.contains(arr[left]))
            {
                left++;
                continue;
            }
            
            if (!vowList.contains(arr[right]))
            {
                right--;
                continue;
            }
            
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
        
        return new String(arr);
    }
}
