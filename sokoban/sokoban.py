import os
import msvcrt



def drawMap(map):
    for line in map:
        for char in line:
            print(char, end="")
        print()



def setVariables(map):
    global playerY, playerX
    targetsLeft = 0
    height = len(map)
    width = len(map[0])

    for i in range(height):
        for j in range(width):
            if map[i][j] == "@":
                playerY = i
                playerX = j

            elif map[i][j] == ".":
                targetsLeft += 1

    return targetsLeft

    


def move(deltaY, deltaX, map):

    global playerY, playerX
    global movesCounter
    global targetsLeft
    y = playerY + deltaY
    x = playerX + deltaX

    #wall
    if map[y][x] == "#":
        return
    

    #empty
    elif map[y][x] == " ":

        movesCounter += 1

        if map[playerY][playerX] == "@":
            map[playerY][playerX] = " "
        else:
            map[playerY][playerX] = "."

        playerY = y
        playerX = x
        map[playerY][playerX] = "@"
        return
    

    #box
    elif map[y][x] in ("$", "*"):

        y2 = playerY + (deltaY * 2)
        x2 = playerX + (deltaX * 2)


        if map[y2][x2] == " ":

            movesCounter += 1

            if map[y][x] == "*":
 
                targetsLeft += 1

            if map[playerY][playerX] == "@":
                map[playerY][playerX] = " "
            else:
                map[playerY][playerX] = "."

            playerY = y
            playerX = x
            if map[playerY][playerX] == "$":
                map[playerY][playerX] = "@"
            else:
                map[playerY][playerX] = "+"
            map[y2][x2] = "$"

            
        elif map[y2][x2] == ".":

            movesCounter += 1

            if map[y][x] != "*":
                targetsLeft -= 1

            if map[playerY][playerX] == "@":
                map[playerY][playerX] = " "
            else:
                map[playerY][playerX] = "."

            playerY = y
            playerX = x
            if map[playerY][playerX] == "$":
                map[playerY][playerX] = "@"
            else:
                map[playerY][playerX] = "+"
            map[y2][x2] = "*"
        return


    #target
    elif map[y][x] == ".":

        movesCounter += 1

        if map[playerY][playerX] == "@":
            map[playerY][playerX] = " "
        else:
            map[playerY][playerX] = "."

    playerY = y
    playerX = x
    map[playerY][playerX] = "+"
    return




playerY = 0
playerX = 0
targetsLeft = 0
movesCounter = 0

def main():
    if os.path.exists("map.txt"):
        file = open("map.txt", "r")


        moves = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

        map = []
        for line in file:
            map.append(list(line.rstrip('\n')))

        global targetsLeft
        targetsLeft = setVariables(map)


        key = ""
        while targetsLeft > 0 and key != "q":
            os.system("cls")
            drawMap(map)

            key = msvcrt.getch()
            key = key.decode()
            if key.lower() in moves:
                move(*moves[key.lower()], map)


        if targetsLeft == 0:
            os.system("cls")        
            print("Zwyciestwo!")
            global movesCounter
            print("Ilosc ruchow: ", movesCounter)



        file.close()


    else: 
        print("ERROR: nie znaleziono pliku z mapa")


if __name__ == "__main__":
    main()
