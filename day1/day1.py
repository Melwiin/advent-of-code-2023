file = open("day1/input.txt")
lines = file.readlines()

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def findSolutionP2():
    calibrationValues = []
    for line in lines:
        numbers = []

        print(line)
        for index, num in enumerate(nums):
            wheres = find_all(line, num)
            if wheres != []:
                for where in wheres:
                    line = list(line)
                    line[where + 1] = str(index + 1)
                    line = ''.join(line)
        print(line + " \n")

        # 53594 -> 53592

        for char in line:
            if char.isdigit():
                numbers.append(char)

        if len(numbers) == 1:
            calibrationValues.append(int('{0}{1}'.format(numbers[0], numbers[0])))
        elif len(numbers) == 0:
            continue
        else:
            calibrationValues.append(int('{0}{1}'.format(numbers[0], numbers[-1])))

    result = sum(calibrationValues)
    return result
        

def findSolution():
    calibrationValues = []
    for line in lines:
        numbers = []

        for char in line:
            if char.isdigit():
                numbers.append(char)

        if len(numbers) == 1:
            calibrationValues.append(int('{0}{1}'.format(numbers[0], numbers[0])))
        elif len(numbers) == 0:
            continue
        else:
            calibrationValues.append(int('{0}{1}'.format(numbers[0], numbers[-1])))

    result = sum(calibrationValues)
    return result

print("P1: ", findSolution())
print("P2: ", findSolutionP2())