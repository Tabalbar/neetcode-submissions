class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_speed = sorted([(a[0],a[1]) for a in zip(position, speed)], reverse=True)
        finish_time = []
        print(pos_to_speed)
        for p, s in pos_to_speed:
            time = (target - p)/s
            if finish_time and time <= finish_time[-1]:
                pass
            else:
                finish_time.append(time)
        return len(finish_time)
