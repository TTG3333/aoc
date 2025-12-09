class SmartPopList(list):
    def __init__(self, *args, **kwargs):
        self._popped_indices = set()
        super().__init__(*args, **kwargs)

    def pop(self, index=-1):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        self._popped_indices.add(index)
        return self[index]

    def pop_all(self):
        for index in sorted(self._popped_indices, reverse=True):
            super().pop(index)
        self._popped_indices.clear()

class RangeManager:
    def __init__(self):
        self.ranges = SmartPopList()

    def add_range(self, new_range_min, new_range_max):
        overlapping_start = None
        overlapping_end = None
        for i, (min, max) in enumerate(self.ranges):
            if min <= new_range_min <= max:
                overlapping_start = i
                break
        for i, (min, max) in enumerate(self.ranges):
            if min <= new_range_max <= max:
                overlapping_end = i
                break
        new_min, new_max = new_range_min, new_range_max
        if overlapping_start is not None:
            min, _ = self.ranges[overlapping_start]
            self.ranges.pop(overlapping_start)
            new_min = min
        if overlapping_end is not None:
            _, max = self.ranges[overlapping_end]
            self.ranges.pop(overlapping_end)
            new_max = max
        self.ranges.pop_all()
        for i, (min, max) in enumerate(self.ranges):
            if new_min <= min <= max <= new_max:
                self.ranges.pop(i)
        self.ranges.pop_all()
        self.ranges.append((new_min, new_max))

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

index = 0
manager = RangeManager()
while index < len(lines) and lines[index] != "":
    start, end = map(int, lines[index].split("-"))
    manager.add_range(start, end)
    index += 1

count = 0
for min, max in manager.ranges:
    count += max - min + 1
print(count)