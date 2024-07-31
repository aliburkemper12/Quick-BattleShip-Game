import random

def main():
    print("         BATTLESHIP")
    print("")
    print("")
    
    col = 9
    row = 9
    
    global arr, userArr
    arr = [["-" for x in range (col + 1)]for y in range (row + 1)]
    userArr = [[" " for x in range (col + 1)]for y in range (row + 1)]
    
    global cell
    global hitCount
    hitCount = 0
    playing = 1
    shipLayout(col, row)

    while(playing):
        if hitCount == 12:
            print("")
            print("")
            print("")
            print("")
            print("           ALL SHIPS SUNK - YOU WON!      ")
            print("")
            print("")
            print("")
            print("")
            print("")
            return
        printBoard(col, row)
        print(hitCount)
        prompt()
        cell = input()
        if cell == "Q":
            return
        num = cell.strip("()")
        targetCell = num.split(",")
        if len(targetCell) < 2:
            print("Invalid")
        elif (targetCell[0] != '9' and targetCell[0] != '8' and targetCell[0] != '7' and targetCell[0] != '6' and targetCell[0] != '5' and targetCell[0] != '4' and targetCell[0] != '3' and targetCell[0] != '2' and targetCell[0] != '1') or (targetCell[1] != '9' and targetCell[1] != '8' and targetCell[1] != '7' and targetCell[1] != '6' and targetCell[1] != '5' and targetCell[1] != '4' and targetCell[1] != '3' and targetCell[1] != '2' and targetCell[1] != '1'):
            print("Invalid")
        else:
            findCell(int(targetCell[0]), int(targetCell[1]))
    
    
        
def printBoard(col, row):
    for x in range (col):
        print("   ", end="")
        print(x+1, end="")
        
    print("")
        
    for x in range (row):
        print(x+1, end="")
        for y in range (col):
            print("| ", end="")
            print(userArr[y][x], "", end="")
        print("|")
        for z in range (row):
            print(" ", end="")
        print("")
        
        
def shipLayout(col, row):
    # lay 4x1 ship first
    origin_x = random.randrange(0, col)
    origin_y = random.randrange(0, row)
    
    # verticle or horizontal
    # 1 verticle 0 horizontal
    foo = [0, 1]
    orientation = random.choice(foo)
    
    # lay 4x1 ship
    if orientation == 0:
        if origin_x > 5:
            arr[origin_x][origin_y] = "x"
            arr[origin_x - 1][origin_y] = "x"
            arr[origin_x - 2][origin_y] = "x"
            arr[origin_x - 3][origin_y] = "x"
            
        elif origin_x <= 5:
            arr[origin_x][origin_y] = "x"
            arr[origin_x + 1][origin_y] = "x"
            arr[origin_x + 2][origin_y] = "x"
            arr[origin_x + 3][origin_y] = "x"
            
    elif orientation == 1:
        if origin_y > 5:
            arr[origin_x][origin_y] = "x"
            arr[origin_x][origin_y - 1] = "x"
            arr[origin_x][origin_y - 2] = "x"
            arr[origin_x][origin_y - 3] = "x"
            
        elif origin_y <= 5:
            arr[origin_x][origin_y] = "x"
            arr[origin_x][origin_y + 1] = "x"
            arr[origin_x][origin_y + 2] = "x"
            arr[origin_x][origin_y + 3] = "x"
        
    count = 0
    while 1:
        val = layoutHelper(col, row)
        if val == 1:
            count = count + 1
        if count == 2:
            break
                
    while 1:
        val = layoutHelperSmall(col, row)
        if val == 1:
            break
        
    
def layoutHelper(col, row):
    # lay 3x1 ship next
    origin_x = random.randrange(0, col)
    origin_y = random.randrange(0, row)
    
    # verticle or horizontal
    # 1 verticle 0 horizontal
    foo = [0, 1]
    orientation = random.choice(foo)
    isSafe = 0
    
    # check if there is a valid use case
    if orientation == 0:
        if origin_x >=2 and arr[origin_x][origin_y] == "-" and arr[origin_x - 1][origin_y] == "-" and arr[origin_x - 2][origin_y] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x - 1][origin_y] = "x"
            arr[origin_x - 2][origin_y] = "x"
            return 1
            
        elif origin_x <=6 and arr[origin_x][origin_y] == "-" and arr[origin_x + 1][origin_y] == "-" and arr[origin_x + 2][origin_y] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x + 1][origin_y] = "x"
            arr[origin_x + 2][origin_y] = "x"  
            return 1     
    
    if orientation == 1 or isSafe == 0:
        if origin_y >=2 and arr[origin_x][origin_y] == "-" and arr[origin_x][origin_y - 1] == "-" and arr[origin_x][origin_y - 2] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x][origin_y - 1] = "x"
            arr[origin_x][origin_y - 2] = "x"   
            return 1
            
        elif origin_y <=6 and arr[origin_x][origin_y] == "-" and arr[origin_x][origin_y + 1] == "-" and arr[origin_x][origin_y + 2] == "-":
                arr[origin_x][origin_y] = "x"
                arr[origin_x][origin_y + 1] = "x"
                arr[origin_x][origin_y + 2] = "x" 
                return 1
            
    else:
        return 0
    
def layoutHelperSmall(col, row):
    # lay 2x1 ship next
    origin_x = random.randrange(0, col)
    origin_y = random.randrange(0, row)
    
    # verticle or horizontal
    # 1 verticle 0 horizontal
    foo = [0, 1]
    orientation = random.choice(foo)
    isSafe = 0
    
    # check if there is a valid use case
    if orientation == 0:
        if origin_x >=1 and arr[origin_x][origin_y] == "-" and arr[origin_x - 1][origin_y] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x - 1][origin_y] = "x"
            return 1
            
        elif origin_x <=7 and arr[origin_x][origin_y] == "-" and arr[origin_x + 1][origin_y] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x + 1][origin_y] = "x" 
            return 1     
    
    if orientation == 1 or isSafe == 0:
        if origin_y >=1 and arr[origin_x][origin_y] == "-" and arr[origin_x][origin_y - 1] == "-":
            arr[origin_x][origin_y] = "x"
            arr[origin_x][origin_y - 1] = "x"  
            return 1
            
        elif origin_y <=7 and arr[origin_x][origin_y] == "-" and arr[origin_x][origin_y + 1] == "-":
                arr[origin_x][origin_y] = "x"
                arr[origin_x][origin_y + 1] = "x" 
                return 1
            
    else:
        return 0
    
def prompt():
    print("Enter target cell, (col, row): [ex: (3, 4)]")
    print("")
    print("Enter Q to quit playing")
    print("")
    
def findCell(targetCol, targetRow):
    if(arr[targetCol][targetRow] == "x"):
        print("")
        print("Hit!")
        print("")
        userArr[targetCol-1][targetRow-1] = "X"
        global hitCount
        hitCount = hitCount + 1
    else:
        print("")
        print("Miss")
        print("")
        userArr[targetCol-1][targetRow-1] = "-"
    
        
    
if __name__=="__main__":
    main()