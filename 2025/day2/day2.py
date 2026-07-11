with open("input.txt") as f:
    line = f.readline()

ranges = line.split(",")
invalids = []

for inputRange in ranges:
    leftRange, rightRange = inputRange.split("-")
    for num in range(int(leftRange), int(rightRange) + 1):
        stringNum = str(num)
        if stringNum[: (len(stringNum) // 2)] == stringNum[(len(stringNum) // 2) :]:
            invalids += [num]

counter = 0
for invalid in invalids:
    counter += invalid
print(counter)
