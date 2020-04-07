class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def difference(time1, time2):
            hours1, minutes1 = time1.split(":")
            hours2, minutes2 = time2.split(":")
            time1 = int(hours1) * 60 + int(minutes1)
            time2 = int(hours2) * 60 + int(minutes2)
            forward_difference = abs(time2 - time1)
            time1 += 24 * 60 #shift earlier time forward 24 hours
            wraparound_difference = abs(time2 - time1)
            return min(forward_difference, wraparound_difference)
            
        min_difference = float("inf")
        timeline = sorted(timePoints)
        
        for i in range(0, len(timeline) - 1):
            min_difference = min(min_difference, difference(timeline[i], timeline[i+1]))
        #also check time between beginning and end of timeline, due to wraparound.
        min_difference = min(min_difference, difference(timeline[0], timeline[-1]))
        
        return min_difference
        