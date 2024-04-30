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

def kleineBootlocatieVraag():
    global abc, kleineBootlocatieVraagTrue
    while kleineBootlocatieVraagTrue is True:

        print("plaats kleine boot twee vakjes dus")

#=============================================================eersteCord================================================================#
        kleineBootlocatie = input("geeft cord 1: ")
        onlyleter1 = re.sub("[^a-zA-Z]", "", kleineBootlocatie)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", kleineBootlocatie)
        if onlyleter1 in abc:

            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":

                    if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                        kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                        print (kleineBootlocatieSavePlayer1)
                    else:
                        kleineBootlocatieSavePlayer1.clear()
                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gebruikt<3")
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

def kleineboot():
    
        global kleineBootlocatieSavePlayer1, kleineBootlocatieVraagTrue
        board()
        kleineBootlocatieVraag()
        kleinebootshipPlaatser()
        kleineBootlocatieSavePlayer1 = kleineBootlocatieSave1Player1
        kleineBootlocatieVraagTrue = True
        board()
        kleineBootlocatieVraag()
        kleinebootshipPlaatser()
        kleineBootlocatieSavePlayer1 = kleineBootlocatieSave2Player1
        kleineBootlocatieVraagTrue = True
        board()
        kleineBootlocatieVraag()
        kleinebootshipPlaatser()
        kleineBootlocatieSavePlayer1 = kleineBootlocatieSave3Player1
        kleineBootlocatieVraagTrue = True
        board()
        kleineBootlocatieVraag()
        kleinebootshipPlaatser()
        kleineBootlocatieSavePlayer1 = kleineBootlocatieSave4Player1
        
        
#=============================================================program==================================================================#
player_select()

if player2 == False:
    kleineboot()
    print(kleineBootlocatieSave1Player1)
    print(kleineBootlocatieSave1Player1)
    print(kleineBootlocatieSave1Player1)
    print(kleineBootlocatieSave1Player1)