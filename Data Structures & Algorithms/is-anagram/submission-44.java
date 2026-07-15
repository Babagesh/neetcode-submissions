class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] alphabets = new int[26];
        for(int i = 0; i < s.length(); i++)
        {
            int chars = s.charAt(i) - 'a';
            int chart = t.charAt(i) - 'a';
            alphabets[chars] += 1;
            alphabets[chart] -= 1;
        }
        for(int n : alphabets)
        {
            if(n != 0)
            {
                return false;
            }
        }
        return true;

    }
}
