class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if (len(self.nums) % 2) == 0:
            left_middle = int(len(self.nums)/2)-1
            right_middle = left_middle + 1
            return (self.nums[left_middle] + self.nums[right_middle])/2
        else:
            middle = int((len(self.nums)-1)//2)
            return self.nums[middle]