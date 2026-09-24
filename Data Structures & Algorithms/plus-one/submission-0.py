class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1 , -1):
            val = (digits[i] + carry)
            if val == 10:
                carry = 1
                val = 0
            else:
                carry = 0
            digits[i] = val
        if carry:
            digits[0] = 1
            digits.append(0)
        return digits