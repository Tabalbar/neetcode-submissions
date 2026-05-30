class Solution:
    def isHappy(self, n: int) -> bool:
        number_found = {}
        str_n = str(n)
        total = 0
        while total != 1:
            total = 0
            for str_num in str_n:
                total += pow(int(str_num),2)
            if total in number_found:
                return False
            else:
                number_found[total] = 1
                str_n = str(total)
        return True