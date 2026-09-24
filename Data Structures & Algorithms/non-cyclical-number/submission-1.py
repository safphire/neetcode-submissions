class Solution:
    def isHappy(self, n: int) -> bool:
        seen =  set()
        squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        num = n
        while True:
            sumSq = 0
            while num > 0:
                sumSq = sumSq + squares[num % 10]
                num = num // 10
            print(sumSq)
            if sumSq == 1:
                return True
            if sumSq in seen:
                break
            else:
                seen.add(sumSq)
            num = sumSq
        return False