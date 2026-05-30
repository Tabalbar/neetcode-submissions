class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_value:
            for val,ts in self.key_value[key][::-1]:
                if ts <= timestamp:
                    return val
            return ""
        else:
            return ""
