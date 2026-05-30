class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_speed = sorted([(a[0],a[1]) for a in zip(position, speed)], reverse=True)
        stack = []
        print(pos_to_speed)
        for p, s in pos_to_speed:
            time = (target - p)/s
            if stack and time <= stack[-1]:
                pass
            else:
                stack.append(time)
        return len(stack)

# ---------2-2
# -------4---4
# ----11111111
# --3--3--3--3
# 1-----------
