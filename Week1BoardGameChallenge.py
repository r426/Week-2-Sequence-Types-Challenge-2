boardSize = int(input("What are the dimensions of your board game?\nEnter one number, e.g. enter 3 for a 3x3 board:"))
cellSize = 3
for i in range(boardSize):
    for j in range(boardSize):
        print(" ", end =" ")
        for k in range(cellSize):
            print("-", end =" ")
    print(" ")
    for j in range(boardSize):
        print("|", end =" ")
        for k in range(cellSize):
            print(" ", end =" ")
    print("|")
for j in range(boardSize):
    print(" ", end =" ")
    for k in range(cellSize):
        print("-", end =" ")
print(" ")