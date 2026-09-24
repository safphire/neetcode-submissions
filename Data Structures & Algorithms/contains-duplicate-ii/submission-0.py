class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        store = set()
        for r in range(len(nums)):
            if r - l > k:
                store.remove(nums[l])
                l += 1
            if nums[r] in store:
                return True
            store.add(nums[r])
        return False
        