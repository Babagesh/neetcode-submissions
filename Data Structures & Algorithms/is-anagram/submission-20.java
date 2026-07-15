class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        // Fill smap and tmap with character counts
        for (int i = 0; i < s.length(); i++) {
            char schar = s.charAt(i);
            smap.put(schar, smap.getOrDefault(schar, 0) + 1);

            char tchar = t.charAt(i);
            tmap.put(tchar, tmap.getOrDefault(tchar, 0) + 1);
        }

        // Compare character counts
        for (char key : smap.keySet()) {
            if (!smap.get(key).equals(tmap.get(key))) {
                return false;
            }
        }

        return true;
    }
}
