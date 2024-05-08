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
<<<<<<< HEAD
=======


drieBootlocatieSavePlayer1 = []
drieBootlocatieSavePlayer2 = []
drieBootlocatieVraagTrue = True

drieBootlocatieSave1Player1 = []
drieBootlocatieSave2Player1 = []
drieBootlocatieSave3Player1 = []
drieBootlocatieSave4Player1 = []


vierBootlocatieSavePlayer1 = []
vierBootlocatieSavePlayer2 = []
vierBootlocatieVraagTrue = True

vierBootlocatieSave1Player1 = []
vierBootlocatieSave2Player1 = []
vierBootlocatieSave3Player1 = []
vierBootlocatieSave4Player1 = []


zesBootlocatieSavePlayer1 = []
zesBootlocatieSavePlayer2 = []
zesBootlocatieVraagTrue = True

zesBootlocatieSave1Player1 = []
zesBootlocatieSave2Player1 = []
zesBootlocatieSave3Player1 = []
zesBootlocatieSave4Player1 = []

all_lists = [kleineBootlocatieSavePlayer1, kleineBootlocatieSavePlayer2, kleineBootlocatieSave1Player1, 
             kleineBootlocatieSave2Player1, kleineBootlocatieSave3Player1, kleineBootlocatieSave4Player1, 
             drieBootlocatieSavePlayer1, drieBootlocatieSavePlayer2, drieBootlocatieSave1Player1, 
             drieBootlocatieSave2Player1, drieBootlocatieSave3Player1, drieBootlocatieSave4Player1, 
             vierBootlocatieSavePlayer1, vierBootlocatieSavePlayer2, vierBootlocatieSave1Player1, 
             vierBootlocatieSave2Player1, vierBootlocatieSave3Player1, vierBootlocatieSave4Player1, 
             zesBootlocatieSavePlayer1, zesBootlocatieSavePlayer2, zesBootlocatieSave1Player1,
             zesBootlocatieSave2Player1, zesBootlocatieSave3Player1, zesBootlocatieSave4Player1]
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903

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
<<<<<<< HEAD
    global abc, kleineBootlocatieVraagTrue
=======
    global abc, kleineBootlocatieVraagTrue, kleineBootlocatieSavePlayer1
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
    while kleineBootlocatieVraagTrue is True:
        kleineBootlocatieSavePlayer1.clear()
        print("plaats kleine boot", bootcountklein ,"twee vakjes dus")

#=============================================================eersteCord================================================================#
        kleineBootlocatie1 = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", kleineBootlocatie)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", kleineBootlocatie)
        if onlyleter1 in abc:
<<<<<<< HEAD
            print("only letter1 in  abc work")
=======
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
            if len(onlyleter1) == 1:
                print("only letter1 = 1 work")
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
<<<<<<< HEAD
                    print("only number1 in 1-10 work")
                    if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                        print("kleinbootlocatie not in kleinbootlocatiesave work")
                        print(bootcountklein)
                        kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                        print (kleineBootlocatieSavePlayer1)
                        if bootcountklein == 1:
                            print("1 work pleas")
                            kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                        elif bootcountklein == 2:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0]:
                                print("zorg ervoor dat de booten niet op elkaarstaan")
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(kleineBootlocatie)
                        elif bootcountklein == 3:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0]:
                                print("zorg ervoor dat de booten niet op elkaarstaan")
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave3Player1.append(kleineBootlocatie)
                        elif bootcountklein == 4:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0]:
                                print("zorg ervoor dat de booten niet op elkaarstaan")
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave4Player1.append(kleineBootlocatie)
=======
                    if kleineBootlocatie1 not in kleineBootlocatieSavePlayer1 or kleineBootlocatie1 not in kleineBootlocatieSavePlayer2:
                        print(bootcountklein)
                        kleineBootlocatieSavePlayer1.append(kleineBootlocatie1)
                        print (kleineBootlocatieSavePlayer1)
                        if bootcountklein == 1:
                            kleineBootlocatieSave1Player1.append(kleineBootlocatie1)
                        elif bootcountklein == 2:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0]:
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(kleineBootlocatie1)
                        elif bootcountklein == 3:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0]:
                                continue
                            else:
                                kleineBootlocatieSave3Player1.append(kleineBootlocatie1)
                        elif bootcountklein == 4:
                            if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0]:
                                continue
                            else:
                                kleineBootlocatieSave4Player1.append(kleineBootlocatie1)
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
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
                                        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 or kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                                            kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 1 or abc.index(onlyleter2) == abc.index(onlyleter1) - 1 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountklein == 1:
<<<<<<< HEAD
                                                    print("1 work pleas")
                                                    kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 2:
                                                        if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            kleineBootlocatieSavePlayer1.clear()
=======
                                                    kleineBootlocatieSave1Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 2:
                                                        print(kleineBootlocatieSavePlayer1)
                                                        if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1]:
                                                            kleineBootlocatieSavePlayer1.remove(kleineBootlocatie)
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
                                                            continue
                                                        else:
                                                            kleineBootlocatieSave2Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 3:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
<<<<<<< HEAD
                                                        kleineBootlocatieSavePlayer1.clear()
=======
                                                        kleineBootlocatieSave1Player1.append(kleineBootlocatie)
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
                                                        continue
                                                    else:
                                                        kleineBootlocatieSave3Player1.append(kleineBootlocatie)
                                                elif bootcountklein == 4:
                                                    if kleineBootlocatie == kleineBootlocatieSave1Player1[0] or kleineBootlocatie == kleineBootlocatieSave2Player1[0] or kleineBootlocatie == kleineBootlocatieSave3Player1[0] or kleineBootlocatie == kleineBootlocatieSave1Player1[1] or kleineBootlocatie == kleineBootlocatieSave2Player1[1] or kleineBootlocatie == kleineBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
<<<<<<< HEAD
                                                        kleineBootlocatieSavePlayer1.clear()
=======
                                                        kleineBootlocatieSave1Player1.append(kleineBootlocatie)
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
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
                                        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 or kleineBootlocatie not in kleineBootlocatieSavePlayer2:
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

<<<<<<< HEAD
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

def start():
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
        
=======
def shipPlaatser(shipCords):#intenet moet nog eens doorlezen!!!
    for coord in shipCords:
        row = coord[0]  # Extract the row letter
        col = int(coord[1:])  # Extract the column number
        # Update the corresponding cell with 'O'
        globals()[row + str(col)] = 'O'

def printy():
    global x
    x = 0
    for lst in all_lists:
        print(lst),print(x)
        x = x + 1

def start1player():
    global kleineBootlocatieVraagTrue, kleineBootlocatieSavePlayer1 
    board()
    kleineBootlocatieVraag(1)
    shipPlaatser(kleineBootlocatieSavePlayer1)
    printy()
    kleineBootlocatieVraagTrue = True
    board()
    kleineBootlocatieVraag(2)
    shipPlaatser(kleineBootlocatieSavePlayer1)
    printy()
    kleineBootlocatieVraagTrue = True
    board()
    kleineBootlocatieVraag(3)
    shipPlaatser(kleineBootlocatieSavePlayer1)
    printy()
    kleineBootlocatieVraagTrue = True
    board()
    kleineBootlocatieVraag(4)
    shipPlaatser(kleineBootlocatieSavePlayer1)


def boot3Player1():
    global drieBootlocatieVraagTrue ,drieBootlocatieSavePlayer1
    board()
    drieBootlocatieVraag(1)
    shipPlaatser(drieBootlocatieSavePlayer1)
    drieBootlocatieVraagTrue = True
    board()
    drieBootlocatieVraag(2)
    shipPlaatser(drieBootlocatieSavePlayer1)
    drieBootlocatieVraagTrue = True
    board()
    drieBootlocatieVraag(3)
    shipPlaatser(drieBootlocatieSavePlayer1)

def boot4Player1():
    global vierBootlocatieVraagTrue ,vierBootlocatieSavePlayer1
    board()
    vierBootlocatieVraag(1)
    shipPlaatser(vierBootlocatieSavePlayer1)
    vierBootlocatieVraagTrue = True
    board()
    vierBootlocatieVraag(2)
    shipPlaatser(vierBootlocatieSavePlayer1)

def boot6Players():
    global zesBootlocatieVraagTrue ,zesBootlocatieSavePlayer1
    board()
    zesBootlocatieVraag(1)
    shipPlaatser(zesBootlocatieSavePlayer1)

#=============================================================boot3groot===============================================================#
def drieBootlocatieVraag(bootcountdrie):
    global abc, drieBootlocatieVraagTrue, middelDrie, middelDrieLetter
    while drieBootlocatieVraagTrue is True:
        drieBootlocatieSavePlayer1.clear()
        print("plaats drie boot", bootcountdrie ,"drie vakjes dus")

#=============================================================eersteCord===============================================================#
        drieBootlocatie1 = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", drieBootlocatie1)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", drieBootlocatie1)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if drieBootlocatie1 not in kleineBootlocatieSavePlayer1 or drieBootlocatie1 not in kleineBootlocatieSavePlayer2:
                        drieBootlocatieSavePlayer1.append(drieBootlocatie1)

                        if bootcountdrie == 1:
                            drieBootlocatieSave1Player1.append(drieBootlocatie1)
                        elif bootcountdrie == 2:
                            if drieBootlocatie1 == drieBootlocatieSave1Player1[0]:
                                drieBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(drieBootlocatie1)
                        elif bootcountdrie == 3:
                            if drieBootlocatie1 == drieBootlocatieSave1Player1[0] or drieBootlocatie1 == drieBootlocatieSave2Player1[0]:
                                drieBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                drieBootlocatieSave3Player1.append(drieBootlocatie1)
                        elif bootcountdrie == 4:
                            if drieBootlocatie1 == drieBootlocatieSave1Player1[0] or drieBootlocatie1 == drieBootlocatieSave2Player1[0] or drieBootlocatie1 == drieBootlocatieSave3Player1[0]:
                                drieBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                drieBootlocatieSave4Player1.append(drieBootlocatie1)
                    else:
                        
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
                                        if drieBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatie not in drieBootlocatieSavePlayer2 or drieBootlocatie not in kleineBootlocatieSavePlayer1 or drieBootlocatie not in kleineBootlocatieSavePlayer2:
                                            drieBootlocatieSavePlayer1.append(drieBootlocatie)
                                            print (drieBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 2 or abc.index(onlyleter2) == abc.index(onlyleter1) - 2 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountdrie == 1:
                                                    print(drieBootlocatie1)
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

                                                drieBootlocatieSavePlayer1.append(drieBootlocatie)
                                                middelDrieNumber = int(onlyNumber2) - 1
                                                index = abc.index(onlyleter2)  # Get the index of onlyleter2 in the abc list
                                                preceding_letter = abc[index]  # Get the preceding letter
                                                middelDrie = preceding_letter + str(middelDrieNumber)
                                                drieBootlocatieSavePlayer1.append(middelDrie)
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
                                        if drieBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatie not in drieBootlocatieSavePlayer2:
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

                                                drieBootlocatieSavePlayer1.append(drieBootlocatie)
                                                middelDrieNumber = int(onlyNumber2) 
                                                index = abc.index(onlyleter2)  
                                                preceding_letter = abc[index - 1] 
                                                middelDrie = preceding_letter + str(middelDrieNumber)
                                                drieBootlocatieSavePlayer1.append(middelDrie)
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

#=============================================================boot4groot===============================================================#
def vierBootlocatieVraag(bootcountvier):
    global abc, vierBootlocatieVraagTrue, middelDrie, middelDrieLetter
    while vierBootlocatieVraagTrue is True:
        vierBootlocatieSavePlayer1.clear()
        print("plaats drie boot", bootcountvier ,"vier vakjes dus")

#=============================================================eersteCord===============================================================#
        vierBootlocatie1 = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", vierBootlocatie1)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", vierBootlocatie1)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if vierBootlocatie1 not in kleineBootlocatieSavePlayer1 or vierBootlocatie1 not in kleineBootlocatieSavePlayer2 or vierBootlocatie1 not in drieBootlocatieSavePlayer1 or vierBootlocatie1 not in drieBootlocatieSavePlayer2:
                        vierBootlocatieSavePlayer1.append(vierBootlocatie1)

                        if bootcountvier == 1:
                            vierBootlocatieSave1Player1.append(vierBootlocatie1)
                        elif bootcountvier == 2:
                            if vierBootlocatie1 == vierBootlocatieSave1Player1[0]:
                                vierBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                vierBootlocatieSave2Player1.append(vierBootlocatie1)
                        elif bootcountvier == 3:
                            if vierBootlocatie1 == vierBootlocatieSave1Player1[0] or vierBootlocatie1 == vierBootlocatieSave2Player1[0]:
                                vierBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                vierBootlocatieSave3Player1.append(vierBootlocatie1)
                        elif bootcountvier == 4:
                            if vierBootlocatie1 == vierBootlocatieSave1Player1[0] or vierBootlocatie1 == vierBootlocatieSave2Player1[0] or vierBootlocatie1 == vierBootlocatieSave3Player1[0]:
                                vierBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                vierBootlocatieSave4Player1.append(vierBootlocatie1)
                    else:
                        
                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                        continue
#=============================================================tweedeCord===============================================================#
                    vierBootlocatie = input("geeft cord 2: ")
                    onlyleter2 = re.sub("[^a-zA-Z]", "", vierBootlocatie)
                    onlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", vierBootlocatie)
                    if onlyleter2 in abc:
                        if len(onlyleter2) == 1:
                            if len(onlyNumber2) == 1 or onlyNumber2 == "10":
                                if onlyleter1 == onlyleter2:
                                    if int(onlyNumber2) == int(onlyNumber1) + 3 or int(onlyNumber2) == int(onlyNumber1) - 3:
                                        if vierBootlocatie not in vierBootlocatieSavePlayer1 or vierBootlocatie not in vierBootlocatieSavePlayer2 or vierBootlocatie not in kleineBootlocatieSavePlayer1 or vierBootlocatie not in kleineBootlocatieSavePlayer2 or vierBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatieSavePlayer2:
                                            vierBootlocatieSavePlayer1.append(vierBootlocatie)
                                            print (vierBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 3 or abc.index(onlyleter2) == abc.index(onlyleter1) - 3 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountvier == 1:
                                                    print(vierBootlocatie1)
                                                    vierBootlocatieSave1Player1.append(vierBootlocatie)
                                                elif bootcountvier == 2:
                                                        if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            vierBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            vierBootlocatieSave2Player1.append(vierBootlocatie)
                                                elif bootcountvier == 3:
                                                    if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == vierBootlocatieSave2Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1] or vierBootlocatie == vierBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave3Player1.append(vierBootlocatie)
                                                elif bootcountvier == 4:
                                                    if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == drieBootlocatieSave2Player1[0] or vierBootlocatie == vierBootlocatieSave3Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1] or vierBootlocatie == vierBootlocatieSave2Player1[1] or vierBootlocatie == vierBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave4Player1.append(vierBootlocatie)

                                                vierBootlocatieSavePlayer1.append(vierBootlocatie)
                                                middelVierNumber1 = int(onlyNumber2) - 2
                                                middelVierNumber = int(onlyNumber2) - 1
                                                index = abc.index(onlyleter2)  # Get the index of onlyleter2 in the abc list
                                                preceding_letter = abc[index]  # Get the preceding letter
                                                middelVier = preceding_letter + str(middelVierNumber)
                                                middelVier1 = preceding_letter + str(middelVierNumber1)
                                                vierBootlocatieSavePlayer1.append(middelVier1)
                                                vierBootlocatieSavePlayer1.append(middelVier)
                                                vierBootlocatieVraagTrue = False
                                        else:
                                            vierBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        vierBootlocatieSavePlayer1.clear()
                                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                        continue
                                else:
                                    if int(onlyNumber2) == int(onlyNumber1):
                                        if vierBootlocatie not in vierBootlocatieSavePlayer1 or vierBootlocatie not in vierBootlocatieSavePlayer2 or vierBootlocatie not in kleineBootlocatieSavePlayer1 or vierBootlocatie not in kleineBootlocatieSavePlayer2 or vierBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatieSavePlayer2:
                                            drieBootlocatieSavePlayer1.append(vierBootlocatie)
                                            print (vierBootlocatieSavePlayer1)
            
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 3 or abc.index(onlyleter2) == abc.index(onlyleter1) - 3 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountvier == 1:
                                                    print("1 work pleas")
                                                    vierBootlocatieSave1Player1.append(vierBootlocatie)
                                                elif bootcountvier == 2:
                                                        if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            vierBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            vierBootlocatieSave2Player1.append(vierBootlocatie)
                                                elif bootcountvier == 3:
                                                    if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == vierBootlocatieSave2Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1] or vierBootlocatie == vierBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave3Player1.append(vierBootlocatie)
                                                elif bootcountvier == 4:
                                                    if vierBootlocatie == vierBootlocatieSave1Player1[0] or vierBootlocatie == vierBootlocatieSave2Player1[0] or vierBootlocatie == vierBootlocatieSave3Player1[0] or vierBootlocatie == vierBootlocatieSave1Player1[1] or vierBootlocatie == vierBootlocatieSave2Player1[1] or vierBootlocatie == vierBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave4Player1.append(vierBootlocatie)

                                                vierBootlocatieSavePlayer1.append(vierBootlocatie)
                                                middelVierNumber = int(onlyNumber2) 
                                                index = abc.index(onlyleter2)  
                                                preceding_letter1 = abc[index - 2]
                                                preceding_letter = abc[index - 1] 
                                                middelVier = preceding_letter + str(middelVierNumber)
                                                middelVier1 = preceding_letter1 + str(middelVierNumber)
                                                vierBootlocatieSavePlayer1.append(middelVier)
                                                vierBootlocatieSavePlayer1.append(middelVier1)
                                                vierBootlocatieVraagTrue = False
                                        else:
                                            vierBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        vierBootlocatieSavePlayer1.clear()
                                        print("je kan niet schuin plaatsen")
                                        continue
                            else:
                                vierBootlocatieSavePlayer1.clear()
                                print("zorg dat de y waarde binne de nummer past")
                                continue
                        else:
                            vierBootlocatieSavePlayer1.clear()
                            print("zorg dat je maar 1 letter hebt staan")
                            continue
                    else:
                        vierBootlocatieSavePlayer1.clear()
                        print("zorg dat de x waarde binne de leters past")
                        continue
                else:
                    vierBootlocatieSavePlayer1.clear()
                    print("zorg dat de y waarde binne de leters past")
                    continue
            else:
                vierBootlocatieSavePlayer1.clear()
                print("zorg dat je maar 1 letter hebt staan")
                continue
        else:
            vierBootlocatieSavePlayer1.clear()
            print("zorg dat de x waarde binne de leters past")
            continue

#=============================================================boot6groot===============================================================#
def zesBootlocatieVraag(bootcountzes):
    global abc, zesBootlocatieVraagTrue, middelZes, middelZesLetter
    while zesBootlocatieVraagTrue is True:
        zesBootlocatieSavePlayer1.clear()
        print("plaats zes boot", bootcountzes ,"zes vakjes dus")

#=============================================================eersteCord===============================================================#
        zesBootlocatie1 = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", zesBootlocatie1)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", zesBootlocatie1)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if zesBootlocatie1 not in kleineBootlocatieSavePlayer1 or zesBootlocatie1 not in kleineBootlocatieSavePlayer2 or zesBootlocatie1 not in drieBootlocatieSavePlayer1 or zesBootlocatie1 not in drieBootlocatieSavePlayer2 or zesBootlocatie1 not in vierBootlocatieSavePlayer1 or zesBootlocatie1 not in vierBootlocatieSavePlayer2:
                        zesBootlocatieSavePlayer1.append(zesBootlocatie1)

                        if bootcountzes == 1:
                            zesBootlocatieSave1Player1.append(zesBootlocatie1)
                        elif bootcountzes == 2:
                            if zesBootlocatie1 == zesBootlocatieSave1Player1[0]:
                                zesBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                zesBootlocatieSave2Player1.append(zesBootlocatie1)
                        elif bootcountzes == 3:
                            if zesBootlocatie1 == zesBootlocatieSave1Player1[0] or zesBootlocatie1 == zesBootlocatieSave2Player1[0]:
                                zesBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                zesBootlocatieSave3Player1.append(zesBootlocatie1)
                        elif bootcountzes == 4:
                            if zesBootlocatie1 == zesBootlocatieSave1Player1[0] or zesBootlocatie1 == zesBootlocatieSave2Player1[0] or zesBootlocatie1 == zesBootlocatieSave3Player1[0]:
                                zesBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                zesBootlocatieSave4Player1.append(zesBootlocatie1)
                    else:
                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                        continue
#=============================================================tweedeCord===============================================================#
                    zesBootlocatie = input("geeft cord 2: ")
                    onlyleter2 = re.sub("[^a-zA-Z]", "", zesBootlocatie)
                    onlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", zesBootlocatie)
                    if onlyleter2 in abc:
                        if len(onlyleter2) == 1:
                            if len(onlyNumber2) == 1 or onlyNumber2 == "10":
                                if onlyleter1 == onlyleter2:
                                    if int(onlyNumber2) == int(onlyNumber1) + 5 or int(onlyNumber2) == int(onlyNumber1) - 5:
                                        if zesBootlocatie not in zesBootlocatieSavePlayer1 or zesBootlocatie not in vierBootlocatieSavePlayer2 or zesBootlocatie not in kleineBootlocatieSavePlayer1 or zesBootlocatie not in kleineBootlocatieSavePlayer2 or zesBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatieSavePlayer2 or zesBootlocatie not in vierBootlocatieSavePlayer1 or zesBootlocatie not in vierBootlocatieSavePlayer2:
                                            zesBootlocatieSavePlayer1.append(zesBootlocatie)
                                            print (zesBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 5 or abc.index(onlyleter2) == abc.index(onlyleter1) - 5 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountzes == 1:
                                                    print(zesBootlocatie1)
                                                    vierBootlocatieSave1Player1.append(zesBootlocatie)
                                                elif bootcountzes == 2:
                                                        if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            zesBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            zesBootlocatieSave2Player1.append(zesBootlocatie)
                                                elif bootcountzes == 3:
                                                    if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave2Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1] or zesBootlocatie == zesBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        zesBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        zesBootlocatieSave3Player1.append(zesBootlocatie)
                                                elif bootcountzes == 4:
                                                    if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave2Player1[0] or zesBootlocatie == zesBootlocatieSave3Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1] or zesBootlocatie == zesBootlocatieSave2Player1[1] or zesBootlocatie == zesBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        zesBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        zesBootlocatieSave4Player1.append(zesBootlocatie)

                                                zesBootlocatieSavePlayer1.append(zesBootlocatie)
                                                print("pp")
                                                middelzesNumber1 = int(onlyNumber2) - 4
                                                middelzesNumber2 = int(onlyNumber2) - 3
                                                middelzesNumber3 = int(onlyNumber2) - 2
                                                middelzesNumber4 = int(onlyNumber2) - 1
                                                index = abc.index(onlyleter2)  # Get the index of onlyleter2 in the abc list
                                                preceding_letter = abc[index]  # Get the preceding letter
                                                middelzes4 = preceding_letter + str(middelzesNumber4)
                                                middelzes3 = preceding_letter + str(middelzesNumber3)
                                                middelzes2 = preceding_letter + str(middelzesNumber2)
                                                middelzes1 = preceding_letter + str(middelzesNumber1)
                                                zesBootlocatieSavePlayer1.append(middelzes1)
                                                zesBootlocatieSavePlayer1.append(middelzes2)
                                                zesBootlocatieSavePlayer1.append(middelzes3)
                                                zesBootlocatieSavePlayer1.append(middelzes4)
                                                zesBootlocatieVraagTrue = False
                                        else:
                                            zesBootlocatieSavePlayer1.clear()
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        zesBootlocatieSavePlayer1.clear()
                                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                        continue
                                else:
                                    if int(onlyNumber2) == int(onlyNumber1):
                                        if zesBootlocatie not in zesBootlocatieSavePlayer1 or zesBootlocatie not in vierBootlocatieSavePlayer2 or zesBootlocatie not in kleineBootlocatieSavePlayer1 or zesBootlocatie not in kleineBootlocatieSavePlayer2 or zesBootlocatie not in drieBootlocatieSavePlayer1 or drieBootlocatieSavePlayer2 or zesBootlocatie not in vierBootlocatieSavePlayer1 or zesBootlocatie not in vierBootlocatieSavePlayer2:
                                            zesBootlocatieSavePlayer1.append(zesBootlocatie)
                                            print (zesBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 5 or abc.index(onlyleter2) == abc.index(onlyleter1) - 5 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountzes == 1:
                                                    print(zesBootlocatie1)
                                                    vierBootlocatieSave1Player1.append(zesBootlocatie)
                                                elif bootcountzes == 2:
                                                        if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            zesBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            zesBootlocatieSave2Player1.append(zesBootlocatie)
                                                elif bootcountzes == 3:
                                                    if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave2Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1] or zesBootlocatie == zesBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        zesBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        zesBootlocatieSave3Player1.append(zesBootlocatie)
                                                elif bootcountzes == 4:
                                                    if zesBootlocatie == zesBootlocatieSave1Player1[0] or zesBootlocatie == zesBootlocatieSave2Player1[0] or zesBootlocatie == zesBootlocatieSave3Player1[0] or zesBootlocatie == zesBootlocatieSave1Player1[1] or zesBootlocatie == zesBootlocatieSave2Player1[1] or zesBootlocatie == zesBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        zesBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        zesBootlocatieSave4Player1.append(zesBootlocatie)

                                                zesBootlocatieSavePlayer1.append(zesBootlocatie)
                                                middelzesNumber = int(onlyNumber2) 
                                                index = abc.index(onlyleter2)  
                                                preceding_letter4 = abc[index - 4]
                                                preceding_letter3 = abc[index - 3]
                                                preceding_letter2 = abc[index - 2]
                                                preceding_letter1 = abc[index  - 1] 
                                                middelzes4 = preceding_letter4 + str(middelzesNumber)
                                                middelzes3 = preceding_letter3 + str(middelzesNumber)
                                                middelzes2 = preceding_letter2 + str(middelzesNumber)
                                                middelzes1 = preceding_letter1 + str(middelzesNumber)
                                                zesBootlocatieSavePlayer1.append(middelzes4)
                                                zesBootlocatieSavePlayer1.append(middelzes3)
                                                zesBootlocatieSavePlayer1.append(middelzes2)
                                                zesBootlocatieSavePlayer1.append(middelzes1)
                                                zesBootlocatieVraagTrue = False
                                        else:
                                            zesBootlocatieSavePlayer1.clear()  
                                            print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
                                            continue
                                    else:
                                        zesBootlocatieSavePlayer1.clear()
                                        print("je kan niet schuin plaatsen")
                                        continue
                            else:
                                zesBootlocatieSavePlayer1.clear()
                                print("zorg dat de y waarde binne de nummer past")
                                continue
                        else:
                            zesBootlocatieSavePlayer1.clear()
                            print("zorg dat je maar 1 letter hebt staan")
                            continue
                    else:
                        zesBootlocatieSavePlayer1.clear()
                        print("zorg dat de x waarde binne de leters past")
                        continue
                else:
                    zesBootlocatieSavePlayer1.clear()
                    print("zorg dat de y waarde binne de leters past")
                    continue
            else:
                zesBootlocatieSavePlayer1.clear()
                print("zorg dat je maar 1 letter hebt staan")
                continue
        else:
            zesBootlocatieSavePlayer1.clear()
            print("zorg dat de x waarde binne de leters past")
            continue

>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
#=============================================================program==================================================================#
player_select()

if player2 == False:
<<<<<<< HEAD
    start()
=======
    start1player()
    boot3Player1()
    boot4Player1()
    boot6Players()
>>>>>>> 0659d6590b02a1bc0726032aaf3d739afc0c8903
