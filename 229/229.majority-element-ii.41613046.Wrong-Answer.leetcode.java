  public class Solution
  {
    public List<Integer> majorityElement(int[] nums)
    {
      List<Integer> result = new ArrayList<Integer>();

      if (nums.length == 0)
      {
        return result;
      }

      int num1 = 0;
      int num2 = 0;
      int count1 = 0;
      int count2 = 0;

      for (int num : nums)
      {
        if (num == num1)
        {
          count1++ ;
        }
        else if (num == num2)
        {
          count2++ ;
        }
        else if (count1 == 0)
        {
          num1 = num;
          count1++ ;
        }
        else if (count2 == 0)
        {
          num2 = num;
          count2++ ;
        }
        else
        {
          count1-- ;
          count2-- ;
        }
      }

      result.add(num1);
      result.add(num2);
      return result;
    }
  }

