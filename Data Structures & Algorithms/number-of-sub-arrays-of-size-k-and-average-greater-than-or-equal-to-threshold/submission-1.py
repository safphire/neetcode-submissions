class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        windowSum = 0
        avgCnt = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                windowSum -= arr[l]
                l+=1
            windowSum += arr[r]
            if r-l + 1 == k and windowSum // k >= threshold:
                avgCnt += 1
        return avgCnt
        