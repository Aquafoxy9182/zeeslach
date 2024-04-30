
values = [" "," "," "," "," "," "," "," "," "," "]
listrow = ["a","b","c","d","e","f","g","h","i","j"]
abc = 0
row = 0
x = 1

def board():
    global row ,abc, x

    while x < 10:
        if row == 10:
            b = b + 1
            if b == len(listrow):
                print("lol")
            abc = listrow[b]
            row = 0
            x = x + 1

        else:
            for i, value in enumerate(values):
                globals()[listrow[abc] + str(i)] = value
                row = row + 1

            for i in range(len(values)):
                print(globals()[listrow[abc] + str(i)], "|" , end=" ")
                print(row)



board()