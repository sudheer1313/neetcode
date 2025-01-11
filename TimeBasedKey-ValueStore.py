


class TimeMap:

    def __init__(self):
        self.d = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = dict()
        if timestamp not in self.d[key]:
            self.d[key][timestamp] = []
        self.d[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        count = 0
        for i in self.d[key]:
            if i <= timestamp:
                count = max(count, i)
        if count == 0:
            return ""
        else:
            return self.d[key][count][-1]

