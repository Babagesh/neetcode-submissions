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
            if(!smap.containsKey(schar))
            {
                smap.put(schar, 1);
            }
            else
            {
                smap.put(schar, smap.get(schar) + 1);
            }

            char tchar = t.charAt(i);
            if(!tmap.containsKey(tchar))
            {
                tmap.put(tchar, 1);

            }
            else
            {
                tmap.put(tchar, tmap.get(tchar) + 1);
            }
        }

        // Compare character counts
        return smap.equals(tmap);

    }
}
