import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if set(nums)==k:
            return list(set(nums))
        hm={}
        for num in nums:
            hm[num] = hm.get(num, 0)+1
        res=[]
        for num in hm.keys():
            heapq.heappush(res, (hm[num],num))
            if len(res)>k:
                heapq.heappop(res)
            
        r=[]
        for i in range(k):
            r.append(heapq.heappop(res)[1])
        return r
            