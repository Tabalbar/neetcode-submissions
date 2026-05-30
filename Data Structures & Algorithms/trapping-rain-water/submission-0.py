class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        total_area = 0

        left_max_array = [0 for i in range(len(height))]
        right_max_array = [0 for i in range(len(height))]
        minimum_array = [0 for i in range(len(height))]

        height_length = len(height)

        for i in range(height_length):
            left_max = max(left_max, height[i])
            left_max_array[i] = left_max

        for i in range(height_length-1, -1, -1):
            right_max = max(right_max, height[i])
            right_max_array[i] = right_max

        for i in range(height_length):
            minimum_array[i] = min(left_max_array[i],right_max_array[i])

        for i,num in enumerate(minimum_array):
            potential_area = minimum_array[i] - height[i]
            if potential_area > 0:
                total_area += potential_area

        return total_area
