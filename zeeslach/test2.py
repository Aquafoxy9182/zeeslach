values = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
listrow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
row = 0
b = 0
abc = listrow[b]

def board():
    global row, abc, b
    while True:
        if row == 10:
            b = b + 1
            if b == len(listrow):  # Check if b exceeds the length of listrow
                break
            row = 0
            abc = listrow[b]
            print(abc)

        else:
            print("abc is", abc)
            print("row is", row)
            print("b is", b)
            print("")
            row = row + 1

board()