
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (indices.containsKey(difference)) {
                return new int[]{indices.get(difference), i};
            }
            indices.put(nums[i], i);
        }
        return new int[0]; // Return an empty array if no solution is found
    }
}
