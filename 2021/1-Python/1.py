def part1():
    isBigger = 0
    last = 0
    for line in open("./Advent-Of-Code/2021/1-Python/input1.txt", "r"):   
        if int(line) > last:
            isBigger += 1
        last = int(line)
    print(isBigger-1)

def part2():
    numbers = []
    for line in open("./Advent-Of-Code/2021/1-Python/input1.txt", "r"):   
        numbers.append(int(line))
    
    last = sum(numbers[0:3])
    counter = 1
    isBigger = 0
    while counter < len(numbers)-1:
        curr = sum(numbers[counter-1:counter+2])
        if last < curr:
            isBigger += 1
        last = curr
        counter += 1
    print(isBigger)

part1()
part2()