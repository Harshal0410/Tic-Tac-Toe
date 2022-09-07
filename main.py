def sum(a, b, c):
    return a + b + c

def printboard(xstate, ostate):
    zero = "X" if xstate[0] else ("O" if ostate[0] else 0)
    one = "X" if xstate[1] else ("O" if ostate[1] else 1)
    two = "X" if xstate[2] else ("O" if ostate[2] else 2)
    three = "X" if xstate[3] else ("O" if ostate[3] else 3)
    four = "X" if xstate[4] else ("O" if ostate[4] else 4)
    five = "X" if xstate[5] else ("O" if ostate[5] else 5)
    six = "X" if xstate[6] else ("O" if ostate[6] else 6)
    seven = "X" if xstate[7] else ("O" if ostate[7] else 7)
    eight = "X" if xstate[8] else ("O" if ostate[8] else 8)   
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkwin(xstate, ostate):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X win's.")
            return 1
        if(sum(ostate[win[0]], ostate[win[1]], ostate[win[2]]) == 3):
            print("O win's.")
            return 0
    return -1


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to this game.")
    for i in range(0,9):       
        printboard(xstate, ostate)
        if(turn == 1):
            print("X's turn.")
            try:
                value = int(input('Enter a value : '))
                xstate[value] = 1
            except Exception as e:
                print("Please enter a valid number.")
        else:
            print("O's turn.")
            try:
                value = int(input("Enter a value : "))
                ostate[value] = 1
            except Exception as e:
                print("Please enter a valid number.")
        c = checkwin(xstate, ostate)
        if(c != -1):
            print("Match over.")
            break
        
        turn = 1 - turn
    print("The match is a Tie!")