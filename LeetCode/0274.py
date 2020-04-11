class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        
        if not citations or sorted_citations[0] == 0:
            return 0
        if len(citations) == 1 and citations[0] > 0:
            return 1
        
        l, r = 0, len(citations) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if mid + 1 < sorted_citations[mid]:
                l = mid
            elif mid + 1 > sorted_citations[mid]:
                r = mid
            else:
                return mid + 1
        if r + 1 > sorted_citations[r]:
            return r
        else:
            return r + 1