public class Solution {
    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {
        int[] result = new int[nums.length];
        int start = 0, end = nums.length - 1;
        int nextIndex = 0;
        if (a > 0 || (a == 0 && b >= 0)) 
            nextIndex = nums.length - 1;
        if (a < 0 || (a == 0 && b < 0))
            nextIndex = 0;
        double mid = -1 * ((b * 1.0)  / (2.0 * a));
        while (start <= end) {
            if (a > 0 || (a == 0 && b >= 0)) {
                if (Math.abs(mid - nums[start]) > Math.abs(nums[end] - mid)) {
                    int x = nums[start++];
                    result[nextIndex--] = a * x * x + b * x + c;
                }
                else {
                    int x = nums[end--];
                    result[nextIndex--] = a * x * x + b * x + c;
                }
            }
            else if (a < 0 || (a == 0 && b < 0)){
                if (Math.abs(mid - nums[start]) > Math.abs(nums[end] - mid)) {
                    int x = nums[start++];
                    result[nextIndex++] = a * x * x + b * x + c;
                }
                else {
                    int x = nums[end--];
                    result[nextIndex++] = a * x * x + b * x + c;
                }
            }
        }
        return result;
    }
}
