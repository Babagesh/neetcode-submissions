class Solution {
    public boolean hasDuplicate(int[] nums) 
    {
        HashSet<Integer> hash = new HashSet<Integer>();
        for(int n : nums)
        {
            if (hash.contains(n))
            {
                return true;
            }
            else
            {
                hash.add(n);
            }
        }
        return false;
        
    }
}
