class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        is_negative = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple  

        result = -quotient if is_negative else quotient

        return max(INT_MIN, min(INT_MAX, result))

