class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def difference(time1, time2):
            hours1, minutes1 = time1.split(":")
            hours2, minutes2 = time2.split(":")
            time1 = int(hours1) * 60 + int(minutes1)
            time2 = int(hours2) * 60 + int(minutes2)
            return time2 - time1
            
        min_difference = float("inf")
        timeline = sorted(timePoints)
        
        for i in range(1, len(timeline)):
            min_difference = min(min_difference, difference(timeline[i-1], timeline[i]))
        #also check time between beginning and end of timeline, due to wraparound.
        min_difference = min(min_difference, difference(timeline[-1], timeline[0]) + 1440)
        
        return min_difference
        