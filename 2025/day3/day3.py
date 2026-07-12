maxJoltage = 0


def findBiggestValue(data, earlyStop=False):
    biggestValue = 0
    counter = 0
    for value in data:
        if counter == len(data) - 1 and earlyStop:
            break
        if value > biggestValue:
            biggestValue = value
        counter += 1
    return biggestValue


with open("input.txt") as f:
    for bank in f:
        dataBank = []
        for value in bank:
            if value == "\n":
                continue
            dataBank += [int(value)]

        firstDigit = findBiggestValue(dataBank, True)
        firstDigitPosition = dataBank.index(firstDigit) + 1
        maxJoltage += int(
            str(firstDigit) + str(findBiggestValue(dataBank[firstDigitPosition:]))
        )

print(maxJoltage)
