file = open("day2/input.txt")
lines = file.readlines()

def findSolutionP2():
    games = []
    for line in lines:
        line = line.replace("Game ", "");
        gameId = line.split(': ')[0]
        line = line.split(': ')[1];
        line = line.replace("\n", "")
        sets = line.split("; ")
        red = blue = green = 0;
        for set in sets:
            colors = set.split(", ")
            for color in colors:
                color = color.split(" ")
                if color[1] == "red" and int(color[0]) > red:
                    red = int(color[0])
                elif color[1] == "blue" and int(color[0]) > blue:
                    blue = int(color[0])
                elif color[1] == "green" and int(color[0]) > green:
                    green = int(color[0])
        print("GameID: ", gameId, red, green, blue)
        mult = red * green * blue
        games.append(mult)
    print(sum(games))

def findSolutionP1():
    red_allowed = 12
    green_allowed = 13
    blue_allowed = 14

    allowedGames = []

    for line in lines:
        isGameValid = 1
        line = line.replace("Game ", "");
        gameId = line.split(': ')[0]
        line = line.split(': ')[1];
        line = line.replace("\n", "")
        sets = line.split("; ")
        for set in sets:
            red = blue = green = 0;
            colors = set.split(", ")
            for color in colors:
                color = color.split(" ")
                if color[1] == "red":
                    red = int(color[0])
                elif color[1] == "blue":
                    blue = int(color[0])
                elif color[1] == "green":
                    green = int(color[0])
            if red <= red_allowed and blue <= blue_allowed and green <= green_allowed:
                continue
            else:
                isGameValid = 0
                break
        if isGameValid:
            allowedGames.append(int(gameId))
    print("Answer P1: ", sum(allowedGames))

findSolutionP1()
findSolutionP2()