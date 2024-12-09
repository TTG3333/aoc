with open("Input.txt", "tr") as F:
    line = F.read()

class DiskFile:
    def __init__(self, size, id): # File id of -1 will be empty space
        self.id = id
        self.size = size
    
    def __repr__(self): # For debugging
        return f"File({self.size}, {self.id})"
    
    def __eq__(self, other): # This is to enable finding a file in a list
        return self.id == other.id

disk = []
for i, char in enumerate(line):
    if i%2 == 0:
        disk.append(DiskFile(int(char), i//2))
    else:
        disk.append(DiskFile(int(char), -1))
maxID = len(disk) // 2

def mergeEmptySpace(disk): # Checks the whole disk for adjacent empty space files and merges them
    i = 0
    while i < len(disk) - 1:
        if disk[i].id == -1 and disk[i+1].id == -1:
            disk[i].size += disk[i+1].size
            disk.pop(i+1)
        i += 1

toMoveID = maxID
while toMoveID > 0: # No need to move file 0
    toMoveIndex = disk.index(DiskFile(0, toMoveID))
    toMove = disk[toMoveIndex]
    toMoveID -= 1
    i = 0
    while i < toMoveIndex: # We don't want to move a file forwards
        if disk[i].id == -1 and disk[i].size >= toMove.size:
            break
        i += 1
    else: # Only trips if we reach the end of the disk without finding an empty space big enough
        continue
    emptySpace = disk[i]
    if emptySpace.size > toMove.size: # Need to split emptySpace
        emptySpace.size -= toMove.size
        disk.insert(i, DiskFile(toMove.size, toMove.id))
    else: # they have the same size
        emptySpace.id = toMove.id
    toMove.id = -1 # Set the original block to empty space and then merge all empty space files into one
    mergeEmptySpace(disk)

checksum = 0
i = 0
for file in disk:
    checksum += sum(range(i, i+file.size)) * file.id if file.id != -1 else 0
    i += file.size
print(checksum)