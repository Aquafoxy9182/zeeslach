#=============================================================imports==================================================================#
import re

#=============================================================variable=================================================================#
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = [" "]*10
b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = [" "]*10
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = [" "]*10
d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = [" "]*10
e1, e2, e3, e4, e5, e6, e7, e8, e9, e10 = [" "]*10
f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 = [" "]*10
g1, g2, g3, g4, g5, g6, g7, g8, g9, g10 = [" "]*10
h1, h2, h3, h4, h5, h6, h7, h8, h9, h10 = [" "]*10
i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 = [" "]*10
j1, j2, j3, j4, j5, j6, j7, j8, j9, j10 = [" "]*10

abc = ["a","b","c","d","e","f","g","h","i","j"]

player2 = bool

kleineBootlocatieSavePlayer1 = []
kleineBootlocatieSavePlayer2 = []
kleineBootlocatieVraagTrue = True

kleineBootlocatieSave1Player1 = []
kleineBootlocatieSave2Player1 = []
kleineBootlocatieSave3Player1 = []
kleineBootlocatieSave4Player1 = []


drieBootlocatieSavePlayer1 = []
drieBootlocatieSavePlayer2 = []
drieBootlocatieVraagTrue = True

drieBootlocatieSave1Player1 = []
drieBootlocatieSave2Player1 = []
drieBootlocatieSave3Player1 = []
drieBootlocatieSave4Player1 = []

#=============================================================functions=================================================================#
def board():
    print("  ","1","|","2","|","3","|","4","|","5","|","6","|","7","|","8","|","9","|","10")
    print("-"*42)
    print("A|",a1,"|",a2,"|",a3,"|",a4,"|",a5,"|",a6,"|",a7,"|",a8,"|",a9,"|",a10)
    print("-"*42)
    print("B|",b1,"|",b2,"|",b3,"|",b4,"|",b5,"|",b6,"|",b7,"|",b8,"|",b9,"|",b10)
    print("-"*42)
    print("C|",c1,"|",c2,"|",c3,"|",c4,"|",c5,"|",c6,"|",c7,"|",c8,"|",c9,"|",c10)
    print("-"*42)
    print("D|",d1,"|",d2,"|",d3,"|",d4,"|",d5,"|",d6,"|",d7,"|",d8,"|",d9,"|",d10)
    print("-"*42)
    print("E|",e1,"|",e2,"|",e3,"|",e4,"|",e5,"|",e6,"|",e7,"|",e8,"|",e9,"|",e10)
    print("-"*42)
    print("F|",f1,"|",f2,"|",f3,"|",f4,"|",f5,"|",f6,"|",f7,"|",f8,"|",f9,"|",f10)
    print("-"*42)
    print("G|",g1,"|",g2,"|",g3,"|",g4,"|",g5,"|",g6,"|",g7,"|",g8,"|",g9,"|",g10)
    print("-"*42)
    print("H|",h1,"|",h2,"|",h3,"|",h4,"|",h5,"|",h6,"|",h7,"|",h8,"|",h9,"|",h10)
    print("-"*42)
    print("I|",i1,"|",i2,"|",i3,"|",i4,"|",i5,"|",i6,"|",i7,"|",i8,"|",i9,"|",i10)
    print("-"*42)
    print("J|",j1,"|",j2,"|",j3,"|",j4,"|",j5,"|",j6,"|",j7,"|",j8,"|",j9,"|",j10)
    print("-"*42)

def player_select():
    global player2
    gamesoort = input("2players (y/n): ")
    if gamesoort == "y":
        player2 = True
    elif gamesoort == "n":
        player2 = False

#=============================================================kleindeboot===============================================================#
def kleineBootlocatieVraag(bootcountklein):
    global abc, kleineBootlocatieVraagTrue
    while kleineBootlocatieVraagTrue is True:
        kleineBootlocatieSavePlayer1.clear()
        print("plaats kleine boot", bootcountklein ,"twee vakjes dus")

#=============================================================eersteCord================================================================#
        kleineBootlocatie = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", kleineBootlocatie)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", kleineBootlocatie)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                        print(bootcountklein)
                        kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                        print (kleineBootlocatieSavePlayer1)
                        if bootcountklein == 1:
                            kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                        elif bootcountklein == 2:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0]:
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(kleineBootlocatie)
                        elif bootcountklein == 3:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0]:
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave3Player1.append(kleineBootlocatie)
                        elif bootcountklein == 4:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0]:
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave4Player1.append(kleineBootlocatie)
                    else:
                        kleineBootlocatieSavePlayer1.clear()
                        continue

#=============================================================tweedeCord================================================================#
                    kleineBootlocatie = input("geeft cord 2: ")
                    onlyleter2 = re.sub("[^a-zA-Z]", "", kleineBootlocatie)
                    onlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", kleineBootlocatie)
                    if onlyleter2 in abc:
                        if len(onlyleter2) == 1:
                            if len(onlyNumber2) == 1 or onlyNumber2 == "10":
                                if onlyleter1 == onlyleter2:
                                    if int(onlyNumber2) == int(onlyNumber1) + 1 or int(onlyNumber2) == int(onlyNumber1) - 1:
                                        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                                            kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                                            print (kleineBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 1 or abc.index(onlyleter2) == abc.index(onlyleter1) - 1 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountklein == 1:
                                                    kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 2:
                                                        if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            kleineBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            kleineBootlocatieSave2Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 3:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        kleineBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        kleineBootlocatieSave3Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 4:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1] or kleineBootlocatie == kleineBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        kleineBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        kleineBootlocatieSave4Player1.append(kleineBootlocatie)
                                                kleineBootlocatieVraagTrue = False
                                        else:
                                            kleineBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        kleineBootlocatieSavePlayer1.clear()
                                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                        continue
                                else:
                                    if int(onlyNumber2) == int(onlyNumber1):
                                        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                                            kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                                            print (kleineBootlocatieSavePlayer1)
            
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 1 or abc.index(onlyleter2) == abc.index(onlyleter1) - 1 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountklein == 1:
                                                    print("1 work pleas")
                                                    kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 2:
                                                        if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            kleineBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            kleineBootlocatieSave2Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 3:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        kleineBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        kleineBootlocatieSave3Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 4:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1] or kleineBootlocatie == kleineBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        kleineBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        kleineBootlocatieSave4Player1.append(kleineBootlocatie)
                                                kleineBootlocatieVraagTrue = False
                                        else:
                                            kleineBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        kleineBootlocatieSavePlayer1.clear()
                                        print("je kan niet schuin plaatsen")
                                        continue
                            else:
                                kleineBootlocatieSavePlayer1.clear()
                                print("zorg dat de y waarde binne de nummer past")
                                continue
                        else:
                            kleineBootlocatieSavePlayer1.clear()
                            print("zorg dat je maar 1 letter hebt staan")
                            continue
                    else:
                        kleineBootlocatieSavePlayer1.clear()
                        print("zorg dat de x waarde binne de leters past")
                        continue
                else:
                    kleineBootlocatieSavePlayer1.clear()
                    print("zorg dat de y waarde binne de leters past")
                    continue
            else:
                kleineBootlocatieSavePlayer1.clear()
                print("zorg dat je maar 1 letter hebt staan")
                continue
        else:
            kleineBootlocatieSavePlayer1.clear()
            print("zorg dat de x waarde binne de leters past")
            continue

def kleinebootshipPlaatser():#intenet moet nog eens doorlezen!!!
    global kleineBootlocatieSavePlayer1
    for coord in kleineBootlocatieSavePlayer1:
        row = coord[0]  # Extract the row letter
        col = int(coord[1:])  # Extract the column number
        # Update the corresponding cell with 'O'
        globals()[row + str(col)] = 'O'

def printi():
    print(kleineBootlocatieSave1Player1)
    print(kleineBootlocatieSave2Player1)
    print(kleineBootlocatieSave3Player1)
    print(kleineBootlocatieSave4Player1)

def kleinebootshipPlaatser():#intenet moet nog eens doorlezen!!!
    global kleineBootlocatieSavePlayer1
    for coord in kleineBootlocatieSavePlayer1:
        row = coord[0]  # Extract the row letter
        col = int(coord[1:])  # Extract the column number
        # Update the corresponding cell with 'O'
        globals()[row + str(col)] = 'O'

def start1player():
    global kleineBootlocatieVraagTrue
    board()
    kleineBootlocatieVraag(1)
    kleinebootshipPlaatser()
    printi()
    kleineBootlocatieVraagTrue = True
    board()
    kleineBootlocatieVraag(2)
    kleinebootshipPlaatser()
    printi()
    kleineBootlocatieVraagTrue = True
    board()
    kleineBootlocatieVraag(3)
    kleinebootshipPlaatser()
    printi()
    kleineBootlocatieVraagTrue = True
    kleineBootlocatieVraag(4)
    kleinebootshipPlaatser()
    board()
    printi()

#=============================================================boot3groot===============================================================#
def drieBootlocatieVraag(bootcountdrie):
    global abc, drieBootlocatieVraagTrue
    while drieBootlocatieVraagTrue is True:
        drieBootlocatieSavePlayer1.clear()
        print("plaats kleine boot", bootcountdrie ,"twee vakjes dus")

#=============================================================eersteCord===============================================================#
        drieBootlocatie = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", drieBootlocatie)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", drieBootlocatie)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if drieBootlocatie not in drieBootlocatieSavePlayer1 and drieBootlocatie not in drieBootlocatieSavePlayer2:
                        print(bootcountdrie)
                        kleineBootlocatieSavePlayer1.append(drieBootlocatie)
                        print (kleineBootlocatieSavePlayer1)
                        if bootcountdrie == 1:
                            drieBootlocatieSave1Player1.append(drieBootlocatie)
                        elif bootcountdrie == 2:
                            if drieBootlocatie == drieBootlocatieSave1Player1[0]:
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(drieBootlocatie)
                        elif bootcountdrie == 3:
                            if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0]:
                                drieBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave3Player1.append(drieBootlocatie)
                        elif bootcountdrie == 4:
                            if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0] or drieBootlocatie == drieBootlocatieSave3Player1[0]:
                                drieBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                drieBootlocatieSave4Player1.append(drieBootlocatie)
                    else:
                        drieBootlocatieSavePlayer1.clear()
                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                        continue
#=============================================================tweedeCord===============================================================#
                    drieBootlocatie = input("geeft cord 2: ")
                    onlyleter2 = re.sub("[^a-zA-Z]", "", drieBootlocatie)
                    onlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", drieBootlocatie)
                    if onlyleter2 in abc:
                        if len(onlyleter2) == 1:
                            if len(onlyNumber2) == 1 or onlyNumber2 == "10":
                                if onlyleter1 == onlyleter2:
                                    if int(onlyNumber2) == int(onlyNumber1) + 2 or int(onlyNumber2) == int(onlyNumber1) - 2:
                                        if drieBootlocatie not in drieBootlocatieSavePlayer1 and drieBootlocatie not in drieBootlocatieSavePlayer2:
                                            drieBootlocatieSavePlayer1.append(drieBootlocatie)
                                            print (drieBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 2 or abc.index(onlyleter2) == abc.index(onlyleter1) - 2 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountdrie == 1:
                                                    drieBootlocatieSave1Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 2:
                                                        if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            drieBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            drieBootlocatieSave2Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 3:
                                                    if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1] or drieBootlocatie == drieBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        drieBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        drieBootlocatieSave3Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 4:
                                                    if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0] or drieBootlocatie == drieBootlocatieSave3Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1] or drieBootlocatie == drieBootlocatieSave2Player1[1] or drieBootlocatie == drieBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        drieBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        drieBootlocatieSave4Player1.append(drieBootlocatie)

                                                
                                                drieBootlocatieVraagTrue = False
                                        else:
                                            drieBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        drieBootlocatieSavePlayer1.clear()
                                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                        continue
                                else:
                                    if int(onlyNumber2) == int(onlyNumber1):
                                        if drieBootlocatie not in drieBootlocatieSavePlayer1 and drieBootlocatie not in drieBootlocatieSavePlayer2:
                                            drieBootlocatieSavePlayer1.append(drieBootlocatie)
                                            print (drieBootlocatieSavePlayer1)
            
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 2 or abc.index(onlyleter2) == abc.index(onlyleter1) - 2 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountdrie == 1:
                                                    print("1 work pleas")
                                                    drieBootlocatieSave1Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 2:
                                                        if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            drieBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            drieBootlocatieSave2Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 3:
                                                    if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1] or drieBootlocatie == drieBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        drieBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        drieBootlocatieSave3Player1.append(drieBootlocatie)
                                                elif bootcountdrie == 4:
                                                    if drieBootlocatie == drieBootlocatieSave1Player1[0] or drieBootlocatie == drieBootlocatieSave2Player1[0] or drieBootlocatie == drieBootlocatieSave3Player1[0] or drieBootlocatie == drieBootlocatieSave1Player1[1] or drieBootlocatie == drieBootlocatieSave2Player1[1] or drieBootlocatie == drieBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        drieBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        drieBootlocatieSave4Player1.append(drieBootlocatie)
                                                drieBootlocatieVraagTrue = False
                                        else:
                                            drieBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        drieBootlocatieSavePlayer1.clear()
                                        print("je kan niet schuin plaatsen")
                                        continue
                            else:
                                drieBootlocatieSavePlayer1.clear()
                                print("zorg dat de y waarde binne de nummer past")
                                continue
                        else:
                            drieBootlocatieSavePlayer1.clear()
                            print("zorg dat je maar 1 letter hebt staan")
                            continue
                    else:
                        drieBootlocatieSavePlayer1.clear()
                        print("zorg dat de x waarde binne de leters past")
                        continue
                else:
                    drieBootlocatieSavePlayer1.clear()
                    print("zorg dat de y waarde binne de leters past")
                    continue
            else:
                drieBootlocatieSavePlayer1.clear()
                print("zorg dat je maar 1 letter hebt staan")
                continue
        else:
            drieBootlocatieSavePlayer1.clear()
            print("zorg dat de x waarde binne de leters past")
            continue

def driebootshipPlaatser():#intenet moet nog eens doorlezen!!!
    global drieBootlocatieSavePlayer1
    for coord in drieBootlocatieSavePlayer1:
        row = coord[0]  # Extract the row letter
        col = int(coord[1:])  # Extract the column number
        # Update the corresponding cell with 'O'
        globals()[row + str(col)] = 'O'

#=============================================================program==================================================================#
player_select()

if player2 == False:
    start1player()