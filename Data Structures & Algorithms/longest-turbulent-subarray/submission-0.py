class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        seq1 = 0
        seq2 = 0
        maxturb = 0
        for r in range(1, len(arr)):
            if r % 2 == 0:
                if arr[r-1] < arr[r]:
                    seq1 += 1
                else:
                    seq1 = 0
                if arr[r-1] > arr[r]:
                    seq2 += 1
                else:
                    seq2 = 0
            else:
                if arr[r-1] > arr[r]:
                    seq1 += 1
                else:
                    seq1 = 0
                if arr[r-1] < arr[r]:
                    seq2 += 1
                else:
                    seq2 = 0
            maxturb = max(maxturb, max(seq1, seq2))
        return maxturb + 1
