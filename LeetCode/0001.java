class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, ArrayList<Integer>> values = new HashMap<>();// maps values to lists of indices with those values
        for(int i = 0; i < nums.length; i++) {
            if(!values.containsKey(nums[i])) {
                values.put(nums[i], new ArrayList<Integer>());
            }
            values.get(nums[i]).add(i);
            int currentTarget = target - nums[i];
            if(values.containsKey(currentTarget)) {
                for(int indx: values.get(currentTarget)) {
                    if(indx != i) {
                        return new int[]{indx, i};
                    }
                }
            }
        }
        return new int[]{-1, -1};
    }
}