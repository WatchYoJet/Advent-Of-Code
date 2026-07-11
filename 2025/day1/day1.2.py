

f = open("input.txt")

value = 50
count = 0

for line in f:
    orientation = line[0]
    rotation = int(line[1:])
    count += rotation // 100
    rotation -= (rotation // 100) * 100 
    match orientation:
        
        case "R": # right rotation
            if value + rotation >= 100: #over rotation
                value = value + rotation - 100
                count += 1
            else:
                value += rotation
                if value == 0: count += 1
        
        case "L": # left rotation
            if value - rotation < 0:
                # if we have 0 - 1, this prevents from counting +1 
                if value != 0: count += 1 
                value = value - rotation + 100
            else:
                value -= rotation
                if value == 0: count += 1
            
        case _: print("BRR")


print(count)

f.close()
