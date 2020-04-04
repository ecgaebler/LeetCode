class Solution {
    public String reverseStr(String s, int k) {
        int reverseCount = 0;
        int insertIdx = 0;
        StringBuilder str = new StringBuilder();
        for(int i = 0, n = s.length(); i < n; i++) {
            if(reverseCount <= 0) {
                insertIdx = i;
            }
            str.insert(insertIdx, s.charAt(i));
            reverseCount++;
            if(reverseCount >= k) {
                reverseCount = -k;
            } 
        }
        return str.toString();
    }
}