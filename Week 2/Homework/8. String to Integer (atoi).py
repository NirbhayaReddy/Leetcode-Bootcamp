class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        num_str = ''
        for i,c in enumerate(s):
            if i == 0 and c in "+-":
                num_str += c
            elif c.isdigit():
                num_str += c
            else:
                break
        
        try:
            num = int(num_str)
            return max(min(num, 2**31 - 1), -2**31)
        except ValueError:
            return 0