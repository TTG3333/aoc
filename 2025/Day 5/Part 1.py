class RangeManager:
    def __init__(self):
        self.ranges = []
    
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
        if overlapping_start is None and overlapping_end is None:
            self.ranges.append((new_range_min, new_range_max))
        elif overlapping_start is not None and overlapping_end is None:
            min, _ = self.ranges[overlapping_start]
            self.ranges[overlapping_start] = (min, new_range_max)
        elif overlapping_start is None and overlapping_end is not None:
            _, max = self.ranges[overlapping_end]
            self.ranges[overlapping_end] = (new_range_min, max)
        else:
            min_start, _ = self.ranges[overlapping_start]
            _, max_end = self.ranges[overlapping_end]
            self.ranges[overlapping_start] = (min_start, max_end)
            if overlapping_end != overlapping_start:
                self.ranges.pop(overlapping_end)

    def check(self, val):
        for min, max in self.ranges:
            if min <= val <= max:
                return True
        return False

with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

index = 0
manager = RangeManager()
while index < len(lines) and lines[index] != "":
    start, end = map(int, lines[index].split("-"))
    manager.add_range(start, end)
    index += 1
index += 1  # Skip the empty line

count = 0
for line in lines[index:]:
    num = int(line)
    if manager.check(num):
        count += 1
print(count)