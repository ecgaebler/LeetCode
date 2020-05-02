class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        //Keep track of elements e that have been found, by making value at index e negative
        for(int i = 0; i < nums.size(); i++) {
            int e = abs(nums[i]) - 1; //adjust value to prevent index out-of-bounds
            if(nums[e] > 0) {
                nums[e] = -nums[e];
            }
        }
        //search for positive values; their index corresponds to a value that didn't exist in nums
        vector<int> result;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] > 0) {
                result.push_back(i + 1); //readjst value to original value before pushing
            }
        }
        return result;
    }
};