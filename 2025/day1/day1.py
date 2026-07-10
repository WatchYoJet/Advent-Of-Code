from typing import Counter


f = open("input.txt")

value = 50
count = 0

for line in f:
    orientation = line[0]
    rotation = int(line[1:])
    rotation -= (rotation // 100) * 100 
    match orientation:
        
        case "R": # right rotation
            if value + rotation >= 99: #over rotation
                value = value + rotation - 100
            else:
                value += rotation
                
        case "L": # left rotation
            if value - rotation < 0:
                value = value - rotation + 100
            else:
                value -= rotation
            
        case _: print("BRR")

    if value == 0: count += 1

print(count)

f.close()
