import java.util.*;
class Solution {
    public int[] findRightInterval(int[][] intervals) {
        if(intervals.length == 0) {
            int[] result = {};
            return result;
        }
        if(intervals.length == 1) {
            int[] result = {-1};
            return(result);
        }
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        List<Integer> startIndices = new ArrayList<Integer>();
        for(int i = 0; i < intervals.length; i++) {
            indexMap.put(intervals[i][0], i); 
            startIndices.add(intervals[i][0]);
        }
        Collections.sort(startIndices);
        int[] result = new int[intervals.length];
        for(int i = 0; i < intervals.length; i++) {
            int nextIdx = indexMap.get(startIndices.get(nextIndex(startIndices, intervals[i][1])));
            if(intervals[nextIdx][0] >= intervals[i][1]) {
                result[i] = nextIdx;
            } else {
                result[i] = -1;
            }
        }
        return result;
    }
    private int nextIndex(List<Integer> array, int target) {
        int l = 0, r = array.size() - 1;
        int mid;
        while(l + 1 < r) {
            mid = l + (r - l) / 2;
            if(array.get(mid) < target){
                l = mid;
            } else {
                r = mid;
            }
        }
        if(array.get(l) >= target) {
            return l;
        } else {
            return r;
        }
    }
}