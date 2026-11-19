class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num

            count += mp.get(total - k, 0)

            mp[total] = mp.get(total, 0) + 1

        return count