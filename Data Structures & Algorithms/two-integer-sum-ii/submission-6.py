class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers)-1
        while pointer1 <= pointer2:
            num1 = numbers[pointer1]
            num2 = numbers[pointer2]
            res = num1 + num2
            if res > target:
                pointer2 -= 1
            elif res < target:
                pointer1 += 1
            else:
                return [pointer1+1, pointer2+1]
        return None