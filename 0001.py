class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}
        for index, num in enumerate(nums):
            if num not in index_of:
                index_of[num] = []
            index_of[num].append(index)
        for index, num in enumerate(nums):
            second_num = target - num
            if second_num in index_of:
                for second_index in index_of[second_num]:
                    if second_index != index:
                        return [index, second_index]
        return [-1, -1]