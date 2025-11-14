import math

class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    
    INT_MIN, INT_MAX = -2147483648, 2147483647
    
    if dividend == 0:
        return 0
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) ^ (divisor < 0)
    
    dividend, divisor = abs(dividend), abs(divisor)
    
    log_quotient = math.log(dividend) - math.log(divisor)
    quotient = int(math.exp(log_quotient))
    
    if negative:
        quotient = -quotient
        
    return min(max(INT_MIN, quotient), INT_MAX)