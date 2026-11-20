class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        for i in nums:
            count[i]=count.get(i, 0)+1
        result=sorted(count,key=count.get,reverse=True)
        return result[:k]