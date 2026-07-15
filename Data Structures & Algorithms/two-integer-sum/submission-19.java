
public class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        Map<Integer, Integer> diff_index = new HashMap<>();
        for(int i = 0; i < nums.length; i++)
        {
            int difference = target - nums[i];
            if(diff_index.containsKey(difference))
            {
                return new int[]{diff_index.get(difference), i};
            }
            diff_index.put(nums[i], i);

        }
        return new int[0];
    }
}
