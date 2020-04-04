class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        for i, location in enumerate(list1):
            dict1[location] = i
            
        least_sum = float("inf")
        common = []
        for i, location in enumerate(list2):
            if location in dict1:
                index_sum = i + dict1[location]
                if index_sum == least_sum:
                    common.append(location)
                if index_sum < least_sum:
                    least_sum = index_sum
                    common = [location]
        
        return common