public class Solution 
{
    public List<Integer> findDisappearedNumbers(int[] nums) 
    {
        List<Integer> result = new ArrayList<Integer>();
        
        for (int i = 0; i < nums.length; i++)
        {
            if (nums[i] != nums[nums[i] - 1])
            {
                swap(nums, i, nums[i] - 1);
                i--;
            }
        }
        
        for (int i = 0; i < nums.length; i++)
        {
            if (nums[i] != nums[nums[i] - 1])
            {
                result.add(i + 1);
            }
        }
        
        return result;       
    }
    
    public void swap(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

