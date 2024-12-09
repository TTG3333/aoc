with open("Input.txt", "tr") as F:
    line = F.read()

class DiskFile:
    def __init__(self, size, id): # File id of -1 will be empty space
        self.id = id
        self.size = size
    
    def __repr__(self): # For debugging
        return f"File({self.size}, {self.id})"

disk = []
for i, char in enumerate(line):
    if i%2 == 0:
        disk.append(DiskFile(int(char), i//2))
    else:
        disk.append(DiskFile(int(char), -1))

while True:
    toMove = disk.pop()
    while toMove.id == -1: # Clear empty space from the end of the disk
        toMove = disk.pop()
    i = 0
    while toMove.size > 0:
        while i < len(disk):
            if disk[i].id == -1:
                break
            i += 1
        else: # Only trips if we reach the end of the disk without finding an empty space
            break
        emptySpace = disk[i]
        if emptySpace.size > toMove.size: # Need to split emptySpace
            emptySpace.size -= toMove.size
            disk.insert(i, DiskFile(toMove.size, toMove.id))
            toMove.size = 0
        else: # replace emptySpace's ID and update toMove's length
            emptySpace.id = toMove.id
            toMove.size -= emptySpace.size
    else:
        continue
    if toMove.size > 0:
        disk.append(toMove)
    break

checksum = 0
i = 0
for file in disk:
    checksum += sum(range(i, i+file.size)) * file.id if file.id != -1 else 0
    i += file.size
print(checksum)