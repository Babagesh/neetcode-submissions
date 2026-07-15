class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        for(int i = 0; i < s.length(); i++)
        {
            char chars = s.charAt(i);
            char chart = t.charAt(i);
            smap.put(chars, smap.getOrDefault(chars, 0) + 1);
            tmap.put(chart, tmap.getOrDefault(chart, 0) + 1);
        }
        return smap.equals(tmap);

    }
}
