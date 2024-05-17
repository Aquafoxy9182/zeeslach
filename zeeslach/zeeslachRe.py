#=============================================================imports==================================================================#
import re
import random
import map1
import map2
import map3
import map4
import map5

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
oneTwoThree = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

winner = False

bootSavePlayer1 = []
bootSavePlayer2 = []

boot2Save1Player1 = []
boot2Save2Player1 = []
boot2Save3Player1 = []
boot2Save4Player1 = []

boot2Save1Player2 = []
boot2Save2Player2 = []
boot2Save3Player2 = []
boot2Save4Player2 = []

boot3Save1Player1 = []
boot3Save2Player1 = []
boot3Save3Player1 = []
boot3Save4Player1 = []

boot3Save1Player2 = []
boot3Save2Player2 = []
boot3Save3Player2 = []
boot3Save4Player2 = []

boot4Save1Player1 = []
boot4Save2Player1 = []
boot4Save3Player1 = []
boot4Save4Player1 = []

boot4Save1Player2 = []
boot4Save2Player2 = []
boot4Save3Player2 = []
boot4Save4Player2 = []

boot6Save1Player1 = []
boot6Save2Player1 = []
boot6Save3Player1 = []
boot6Save4Player1 = []

boot6Save1Player2 = []
boot6Save2Player2 = []
boot6Save3Player2 = []
boot6Save4Player2 = []

listOfAllPlayer1 = [
    boot2Save1Player1, boot2Save2Player1, boot2Save3Player1, boot2Save4Player1,
    boot3Save1Player1, boot3Save2Player1, boot3Save3Player1, boot3Save4Player1,
    boot4Save1Player1, boot4Save2Player1, boot4Save3Player1, boot4Save4Player1,
    boot6Save1Player1, boot6Save2Player1, boot6Save3Player1, boot6Save4Player1,
]

listOfAllPlayer2 = [
    boot2Save1Player2, boot2Save2Player2, boot2Save3Player2, boot2Save4Player2,
    boot3Save1Player2, boot3Save2Player2, boot3Save3Player2, boot3Save4Player2,
    boot4Save1Player2, boot4Save2Player2, boot4Save3Player2, boot4Save4Player2,
    boot6Save1Player2, boot6Save2Player2, boot6Save3Player2, boot6Save4Player2
]

#=============================================================functions================================================================#
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

def hitboard():
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

#=============================================================boot2====================================================================#
def boot2(bootCount):
    boot2True = True
    while boot2True is True:
        print("plaats kleine boot ",bootCount," deze boot is 2 lang dus de cordianaten mogen aleen 1 vakje vershil hebben")
        boot2Cord1 = input("geef eerste cordianaten: ")
        boot2Cord1 = boot2Cord1.lower()
        boot2Onlyleter1 = re.sub("[^a-zA-Z]", "", boot2Cord1)
        boot2OnlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot2Cord1)
        if boot2Onlyleter1 in abc:
            if len(boot2Onlyleter1) == 1:
                if boot2OnlyNumber1 in oneTwoThree:
                    if boot2Cord1 not in bootSavePlayer1 and boot2Cord1 not in bootSavePlayer2:
                        boot2Cord1 = f"{boot2Onlyleter1}{boot2OnlyNumber1}"
                        bootSavePlayer1.append(boot2Cord1)
                    else:
                        print("zorg ervoor dat de booten niet op elkaar staan ")
                        continue
                else:
                    print("zorg ervoor dat dat de x cordinaten passen op het bord ")
                    continue
            else:
                print("zorg ervoor dat je maar 1 letter ingeeft")
                continue
        else:
            print("zorg ervoor dat dat de y cordinaten passen op het bord ")
            continue

        boot2Cord2 = input("geef tweede cordianaten: ")
        boot2Cord2 = boot2Cord2.lower()
        boot2Onlyleter2 = re.sub("[^a-zA-Z]", "", boot2Cord2)
        boot2OnlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot2Cord2)
        if boot2Onlyleter2 in abc:
            if len(boot2Onlyleter2) == 1:
                if boot2OnlyNumber2 in oneTwoThree:
                    if boot2Cord2 not in bootSavePlayer1 and boot2Cord2 not in bootSavePlayer2:
                        boot2Cord2 = f"{boot2Onlyleter2}{boot2OnlyNumber2}"
                        if boot2Onlyleter1 == boot2Onlyleter2:
                            if int(boot2OnlyNumber1) == int(boot2OnlyNumber2) + 1 or int(boot2OnlyNumber1) == int(boot2OnlyNumber2) - 1:
                                bootSavePlayer1.append(boot2Cord2)
                                if bootCount == 1:
                                    boot2Save1Player1.append(boot2Cord1)
                                    boot2Save1Player1.append(boot2Cord2)
                                elif bootCount == 2:
                                    boot2Save2Player1.append(boot2Cord1)
                                    boot2Save2Player1.append(boot2Cord2)
                                elif bootCount == 3:
                                    boot2Save3Player1.append(boot2Cord1)
                                    boot2Save3Player1.append(boot2Cord2)
                                elif bootCount == 4:
                                    boot2Save4Player1.append(boot2Cord1)
                                    boot2Save4Player1.append(boot2Cord2)
                                boot2True = False
                            else:
                                bootSavePlayer1.pop()
                                print("Je boot is maar 2 vakjes lang")
                                continue
                        else:
                            if int(boot2OnlyNumber1) == int(boot2OnlyNumber2):
                                if  abc.index(boot2Onlyleter2) == abc.index(boot2Onlyleter1) + 1 or abc.index(boot2Onlyleter2) == abc.index(boot2Onlyleter1) - 1:
                                    bootSavePlayer1.append(boot2Cord2)
                                    if bootCount == 1:
                                        boot2Save1Player1.append(boot2Cord1)
                                        boot2Save1Player1.append(boot2Cord2)
                                    elif bootCount == 2:
                                        boot2Save2Player1.append(boot2Cord1)
                                        boot2Save2Player1.append(boot2Cord2)
                                    elif bootCount == 3:
                                        boot2Save3Player1.append(boot2Cord1)
                                        boot2Save3Player1.append(boot2Cord2)
                                    elif bootCount == 4:
                                        boot2Save4Player1.append(boot2Cord1)
                                        boot2Save4Player1.append(boot2Cord2)
                                    boot2True = False
                                else:
                                    print("je mag niet schuin plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                print("je mag niet schuin plaatsen")
                                bootSavePlayer1.pop()
                                continue
                    else:
                        print("zorg ervoor dat de booten niet op elkaar staan ")
                        continue                       
                else:
                    print("zorg ervoor dat dat de x cordinaten passen op het bord ")
                    continue 
            else:
                print("zorg ervoor dat je maar 1 letter ingeeft")
                continue
        else:
            print("zorg ervoor dat dat de y cordinaten passen op het bord ")
            continue

#=============================================================boot3===============================================================#
def boot3(bootCount):
    global bootSavePlayer1, bootSavePlayer2 
    boot3True = True
    while boot3True:
        print("plaats kleine boot ", bootCount, " deze boot is 2 lang dus de coördinaten mogen alleen 1 vakje verschil hebben")
        boot3Cord1 = input("geef eerste coördinaten: ")
        boot3Cord1 = boot3Cord1.lower()
        boot3OnlyLetter1 = re.sub("[^a-zA-Z]", "", boot3Cord1)
        boot3OnlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot3Cord1)
        if boot3OnlyLetter1 in abc:
            if len(boot3OnlyLetter1) == 1:
                if boot3OnlyNumber1 in oneTwoThree:
                    if boot3Cord1 not in bootSavePlayer1 and boot3Cord1 not in bootSavePlayer2:
                        boot3Cord1 = f"{boot3OnlyLetter1}{boot3OnlyNumber1}"
                        bootSavePlayer1.append(boot3Cord1)
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            continue

        boot3Cord2 = input("geef tweede coördinaten: ")
        boot3Cord2 = boot3Cord2.lower()
        boot3OnlyLetter2 = re.sub("[^a-zA-Z]", "", boot3Cord2)
        boot3OnlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot3Cord2)
        if boot3OnlyLetter2 in abc:
            if len(boot3OnlyLetter2) == 1:
                if boot3OnlyNumber2 in oneTwoThree:
                    if boot3Cord2 not in bootSavePlayer1 and boot3Cord2 not in bootSavePlayer2:
                        boot3Cord2 = f"{boot3OnlyLetter2}{boot3OnlyNumber2}"
                        if boot3OnlyLetter1 == boot3OnlyLetter2:
                            if int(boot3OnlyNumber1) == int(boot3OnlyNumber2) + 2 or int(boot3OnlyNumber1) == int(boot3OnlyNumber2) - 2:

                                middel3Number = int(boot3OnlyNumber2) - 1
                                index = abc.index(boot3OnlyLetter2)  # Get the index of boot3OnlyLetter2 in the abc list
                                preceding_letter = abc[index]  # Get the preceding letter
                                middel3 = preceding_letter + str(middel3Number)

                                if middel3 not in bootSavePlayer1 and middel3 not in bootSavePlayer2:
                                    bootSavePlayer1.append(middel3)
                                    bootSavePlayer1.append(boot3Cord2)
                                    if bootCount == 1:
                                        boot3Save1Player1.append(boot3Cord1)
                                        boot3Save1Player1.append(boot3Cord2)
                                        boot3Save1Player1.append(middel3)
                                    elif bootCount == 2:
                                        boot3Save2Player1.append(boot3Cord1)
                                        boot3Save2Player1.append(boot3Cord2)
                                        boot3Save2Player1.append(middel3)
                                    elif    bootCount == 3:
                                        boot3Save3Player1.append(boot3Cord1)
                                        boot3Save3Player1.append(boot3Cord2)
                                        boot3Save3Player1.append(middel3)
                                    elif bootCount == 4:
                                        boot3Save4Player1.append(boot3Cord1)
                                        boot3Save4Player1.append(boot3Cord2)
                                        boot3Save4Player1.append(middel3)
                                    boot3True = False
                                else:
                                    print("je mag de booten niet op elkaar plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                bootSavePlayer1.pop()
                                print("Je boot is maar 2 vakjes lang")
                                continue
                        else:
                            if int(boot3OnlyNumber1) == int(boot3OnlyNumber2):
                                if abc.index(boot3OnlyLetter2) == abc.index(boot3OnlyLetter1) + 2 or abc.index(boot3OnlyLetter2) == abc.index(boot3OnlyLetter1) - 2:

                                    middel3Number = int(boot3OnlyNumber2)
                                    index = abc.index(boot3OnlyLetter2)  # Get the index of boot3OnlyLetter2 in the abc list
                                    preceding_letter = abc[index - 1]  # Get the preceding letter
                                    middel3 = preceding_letter + str(middel3Number)

                                    if middel3 not in bootSavePlayer1 and middel3 not in bootSavePlayer2:
                                        bootSavePlayer1.append(middel3)
                                        bootSavePlayer1.append(boot3Cord2)
                                        if bootCount == 1:
                                            boot3Save1Player1.append(boot3Cord1)
                                            boot3Save1Player1.append(boot3Cord2)
                                            boot3Save1Player1.append(middel3)
                                        elif bootCount == 2:
                                            boot3Save2Player1.append(boot3Cord1)
                                            boot3Save2Player1.append(boot3Cord2)
                                            boot3Save2Player1.append(middel3)
                                        elif bootCount == 3:
                                            boot3Save3Player1.append(boot3Cord1)
                                            boot3Save3Player1.append(boot3Cord2)
                                            boot3Save3Player1.append(middel3)
                                        elif bootCount == 4:
                                            boot3Save4Player1.append(boot3Cord1)
                                            boot3Save4Player1.append(boot3Cord2)
                                            boot3Save4Player1.append(middel3)
                                        boot3True = False
                                    else:
                                        print("je mag de booten niet op elkaar plaatsen")
                                        bootSavePlayer1.pop()
                                        continue
                                else:
                                    print("Je mag niet schuin plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                print("Je mag niet schuin plaatsen")
                                bootSavePlayer1.pop()
                                continue
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        bootSavePlayer1.pop()
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    bootSavePlayer1.pop()
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                bootSavePlayer1.pop()
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            bootSavePlayer1.pop()
            continue

#=============================================================boot4===============================================================#
def boot4(bootCount):
    global bootSavePlayer1, bootSavePlayer2 
    boot4True = True
    while boot4True:
        print("plaats kleine boot ", bootCount, " deze boot is 2 lang dus de coördinaten mogen alleen 1 vakje verschil hebben")
        boot4Cord1 = input("geef eerste coördinaten: ")
        boot4Cord1 = boot4Cord1.lower()
        boot4OnlyLetter1 = re.sub("[^a-zA-Z]", "", boot4Cord1)
        boot4OnlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot4Cord1)
        if boot4OnlyLetter1 in abc:
            if len(boot4OnlyLetter1) == 1:
                if boot4OnlyNumber1 in oneTwoThree:
                    if boot4Cord1 not in bootSavePlayer1 and boot4Cord1 not in bootSavePlayer2:
                        boot4Cord1 = f"{boot4OnlyLetter1}{boot4OnlyNumber1}"
                        bootSavePlayer1.append(boot4Cord1)
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            continue

        boot4Cord2 = input("geef tweede coördinaten: ")
        boot4Cord2 = boot4Cord2.lower()
        boot4OnlyLetter2 = re.sub("[^a-zA-Z]", "", boot4Cord2)
        boot4OnlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot4Cord2)
        if boot4OnlyLetter2 in abc:
            if len(boot4OnlyLetter2) == 1:
                if boot4OnlyNumber2 in oneTwoThree:
                    if boot4Cord2 not in bootSavePlayer1 and boot4Cord2 not in bootSavePlayer2:
                        boot4Cord2 = f"{boot4OnlyLetter2}{boot4OnlyNumber2}"
                        if boot4OnlyLetter1 == boot4OnlyLetter2:
                            if int(boot4OnlyNumber1) == int(boot4OnlyNumber2) + 3 or int(boot4OnlyNumber1) == int(boot4OnlyNumber2) - 3:
                                middel4Number1 = int(boot4OnlyNumber2) - 2
                                middel4Number = int(boot4OnlyNumber2) - 1
                                index = abc.index(boot4OnlyLetter2)
                                preceding_letter = abc[index]
                                middel41 = preceding_letter + str(middel4Number1)
                                middel4 = preceding_letter + str(middel4Number)

                                if middel4 not in bootSavePlayer1 and middel4 not in bootSavePlayer2 or middel41 not in bootSavePlayer1 and middel41 not in bootSavePlayer2:
                                    bootSavePlayer1.append(middel41)
                                    bootSavePlayer1.append(middel4)
                                    bootSavePlayer1.append(boot4Cord2)
                                    if bootCount == 1:
                                        boot4Save1Player1.append(boot4Cord1)
                                        boot4Save1Player1.append(boot4Cord2)
                                        boot4Save1Player1.append(middel4)
                                        boot4Save1Player1.append(middel41)
                                    elif bootCount == 2:
                                        boot4Save2Player1.append(boot4Cord1)
                                        boot4Save2Player1.append(boot4Cord2)
                                        boot4Save2Player1.append(middel4)
                                        boot4Save2Player1.append(middel41)
                                    elif bootCount == 3:
                                        boot4Save3Player1.append(boot4Cord1)
                                        boot4Save3Player1.append(boot4Cord2)
                                        boot4Save3Player1.append(middel4)
                                        boot4Save3Player1.append(middel41)
                                    elif bootCount == 4:
                                        boot4Save4Player1.append(boot4Cord1)
                                        boot4Save4Player1.append(boot4Cord2)
                                        boot4Save4Player1.append(middel4)
                                        boot4Save4Player1.append(middel41)
                                    boot4True = False
                                else:
                                    print("Je mag de boten niet op elkaar plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                bootSavePlayer1.pop()
                                print("Je boot is maar 2 vakjes lang")
                                continue
                        else:
                            if int(boot4OnlyNumber1) == int(boot4OnlyNumber2):
                                if abc.index(boot4OnlyLetter2) == abc.index(boot4OnlyLetter1) + 3 or abc.index(boot4OnlyLetter2) == abc.index(boot4OnlyLetter1) - 3: 
                                    middel4Number = int(boot4OnlyNumber2)
                                    index = abc.index(boot4OnlyLetter2)
                                    preceding_letter1 = abc[index - 2]
                                    preceding_letter = abc[index - 1]
                                    middel41 = preceding_letter1 + str(middel4Number)
                                    middel4 = preceding_letter + str(middel4Number)
                                    if middel4 not in bootSavePlayer1 and middel4 not in bootSavePlayer2 and middel41 not in bootSavePlayer1 and middel41 not in bootSavePlayer2:
                                        bootSavePlayer1.append(middel41)
                                        bootSavePlayer1.append(middel4)
                                        bootSavePlayer1.append(boot4Cord2)
                                        if bootCount == 1:
                                            boot4Save1Player1.append(boot4Cord1)
                                            boot4Save1Player1.append(boot4Cord2)
                                            boot4Save1Player1.append(middel4)
                                            boot4Save1Player1.append(middel41)
                                        elif bootCount == 2:
                                            boot4Save2Player1.append(boot4Cord1)
                                            boot4Save2Player1.append(boot4Cord2)
                                            boot4Save2Player1.append(middel4)
                                            boot4Save2Player1.append(middel41)
                                        elif bootCount == 3:
                                            boot4Save3Player1.append(boot4Cord1)
                                            boot4Save3Player1.append(boot4Cord2)
                                            boot4Save3Player1.append(middel4)
                                            boot4Save3Player1.append(middel41)
                                        elif bootCount == 4:
                                            boot4Save4Player1.append(boot4Cord1)
                                            boot4Save4Player1.append(boot4Cord2)
                                            boot4Save4Player1.append(middel4)
                                            boot4Save4Player1.append(middel41)
                                        boot4True = False
                                    else:
                                        print("Je mag de boten niet op elkaar plaatsen")
                                        bootSavePlayer1.pop()
                                        continue
                                else:
                                    print("Je mag niet schuin plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                print("Je mag niet schuin plaatsen")
                                bootSavePlayer1.pop()
                                continue
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        bootSavePlayer1.pop()
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    bootSavePlayer1.pop()
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                bootSavePlayer1.pop()
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            bootSavePlayer1.pop()
            continue

#=============================================================boot6===============================================================#
def boot6(bootCount):
    global bootSavePlayer1, bootSavePlayer2 
    boot6True = True
    while boot6True:
        print("plaats kleine boot ", bootCount, " deze boot is 2 lang dus de coördinaten mogen alleen 1 vakje verschil hebben")
        boot6Cord1 = input("geef eerste coördinaten: ")
        boot6Cord1 = boot6Cord1.lower()
        boot6OnlyLetter1 = re.sub("[^a-zA-Z]", "", boot6Cord1)
        boot6OnlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot6Cord1)
        if boot6OnlyLetter1 in abc:
            if len(boot6OnlyLetter1) == 1:
                if boot6OnlyNumber1 in oneTwoThree:
                    if boot6Cord1 not in bootSavePlayer1 and boot6Cord1 not in bootSavePlayer2:
                        boot6Cord1 = f"{boot6OnlyLetter1}{boot6OnlyNumber1}"
                        bootSavePlayer1.append(boot6Cord1)
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            continue

        boot6Cord2 = input("geef tweede coördinaten: ")
        boot6Cord2 = boot6Cord2.lower()
        boot6OnlyLetter2 = re.sub("[^a-zA-Z]", "", boot6Cord2)
        boot6OnlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", boot6Cord2)
        if boot6OnlyLetter2 in abc:
            if len(boot6OnlyLetter2) == 1:
                if boot6OnlyNumber2 in oneTwoThree:
                    if boot6Cord2 not in bootSavePlayer1 and boot6Cord2 not in bootSavePlayer2:
                        boot6Cord2 = f"{boot6OnlyLetter2}{boot6OnlyNumber2}"
                        if boot6OnlyLetter1 == boot6OnlyLetter2:
                            if int(boot6OnlyNumber1) == int(boot6OnlyNumber2) + 5 or int(boot6OnlyNumber1) == int(boot6OnlyNumber2) - 5:
                                middelzesNumber1 = int(boot6OnlyNumber2) - 4
                                middelzesNumber2 = int(boot6OnlyNumber2) - 3
                                middelzesNumber3 = int(boot6OnlyNumber2) - 2
                                middelzesNumber4 = int(boot6OnlyNumber2) - 1
                                index = abc.index(boot6OnlyLetter2)
                                preceding_letter = abc[index]
                                middel64 = preceding_letter + str(middelzesNumber1)
                                middel63 = preceding_letter + str(middelzesNumber2)
                                middel62 = preceding_letter + str(middelzesNumber3)
                                middel61 = preceding_letter + str(middelzesNumber4)

                                if middel61 not in bootSavePlayer1 and middel61 not in bootSavePlayer2 and middel62 not in bootSavePlayer1 and middel62 not in bootSavePlayer2 and middel63 not in bootSavePlayer1 and middel63 not in bootSavePlayer2 and middel64 not in bootSavePlayer1 and middel64 not in bootSavePlayer2:
                                    bootSavePlayer1.append(middel64)
                                    bootSavePlayer1.append(middel63)
                                    bootSavePlayer1.append(middel62)
                                    bootSavePlayer1.append(middel61)
                                    bootSavePlayer1.append(boot6Cord2)
                                    if bootCount == 1:
                                        boot6Save1Player1.append(boot6Cord1)
                                        boot6Save1Player1.append(boot6Cord2)
                                        boot6Save1Player1.append(middel61)
                                        boot6Save1Player1.append(middel62)
                                        boot6Save1Player1.append(middel63)
                                        boot6Save1Player1.append(middel64)
                                    elif bootCount == 2:
                                        boot6Save2Player1.append(boot6Cord1)
                                        boot6Save2Player1.append(boot6Cord2)
                                        boot6Save2Player1.append(middel61)
                                        boot6Save2Player1.append(middel62)
                                        boot6Save2Player1.append(middel63)
                                        boot6Save2Player1.append(middel64)
                                    elif bootCount == 3:
                                        boot6Save3Player1.append(boot6Cord1)
                                        boot6Save3Player1.append(boot6Cord2)
                                        boot6Save3Player1.append(middel61)
                                        boot6Save3Player1.append(middel62)
                                        boot6Save3Player1.append(middel63)
                                        boot6Save3Player1.append(middel64)
                                    elif bootCount == 4:
                                        boot6Save4Player1.append(boot6Cord1)
                                        boot6Save4Player1.append(boot6Cord2)
                                        boot6Save4Player1.append(middel61)
                                        boot6Save4Player1.append(middel62)
                                        boot6Save4Player1.append(middel63)
                                        boot6Save4Player1.append(middel64)
                                    boot6True = False
                                else:
                                    print("Je mag de boten niet op elkaar plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                bootSavePlayer1.pop()
                                print("Je boot is maar 2 vakjes lang")
                                continue
                        else:
                            if int(boot6OnlyNumber1) == int(boot6OnlyNumber2):
                                if abc.index(boot6OnlyLetter2) == abc.index(boot6OnlyLetter1) + 5 or abc.index(boot6OnlyLetter2) == abc.index(boot6OnlyLetter1) - 5: 

                                    middel6Number = int(boot6OnlyNumber2)
                                    index = abc.index(boot6OnlyLetter2)
                                    preceding_letter4 = abc[index - 4]
                                    preceding_letter3 = abc[index - 3]
                                    preceding_letter2 = abc[index - 2]
                                    preceding_letter1 = abc[index - 1]
                                    middel64 = preceding_letter4 + str(middel6Number)
                                    middel63 = preceding_letter3 + str(middel6Number)
                                    middel62 = preceding_letter2 + str(middel6Number)
                                    middel61 = preceding_letter1 + str(middel6Number)

                                    if middel61 not in bootSavePlayer1 and middel61 not in bootSavePlayer2 and middel62 not in bootSavePlayer1 and middel62 not in bootSavePlayer2 and middel63 not in bootSavePlayer1 and middel63 not in bootSavePlayer2 and middel64 not in bootSavePlayer1 and middel64 not in bootSavePlayer2:
                                        bootSavePlayer1.append(middel64)
                                        bootSavePlayer1.append(middel63)
                                        bootSavePlayer1.append(middel62)
                                        bootSavePlayer1.append(middel61)
                                        bootSavePlayer1.append(boot6Cord2)
                                        if bootCount == 1:
                                            boot6Save1Player1.append(boot6Cord1)
                                            boot6Save1Player1.append(boot6Cord2)
                                            boot6Save1Player1.append(middel61)
                                            boot6Save1Player1.append(middel62)
                                            boot6Save1Player1.append(middel63)
                                            boot6Save1Player1.append(middel64)
                                        elif bootCount == 2:
                                            boot6Save2Player1.append(boot6Cord1)
                                            boot6Save2Player1.append(boot6Cord2)
                                            boot6Save2Player1.append(middel61)
                                            boot6Save2Player1.append(middel62)
                                            boot6Save2Player1.append(middel63)
                                            boot6Save2Player1.append(middel64)
                                        elif bootCount == 3:
                                            boot6Save3Player1.append(boot6Cord1)
                                            boot6Save3Player1.append(boot6Cord2)
                                            boot6Save3Player1.append(middel61)
                                            boot6Save3Player1.append(middel62)
                                            boot6Save3Player1.append(middel63)
                                            boot6Save3Player1.append(middel64)
                                        elif bootCount == 4:
                                            boot6Save4Player1.append(boot6Cord1)
                                            boot6Save4Player1.append(boot6Cord2)
                                            boot6Save4Player1.append(middel61)
                                            boot6Save4Player1.append(middel62)
                                            boot6Save4Player1.append(middel63)
                                            boot6Save4Player1.append(middel64)
                                        boot6True = False
                                    else:
                                        print("Je mag de boten niet op elkaar plaatsen")
                                        bootSavePlayer1.pop()
                                        continue
                                else:
                                    print("Je mag niet schuin plaatsen")
                                    bootSavePlayer1.pop()
                                    continue
                            else:
                                print("Je mag niet schuin plaatsen")
                                bootSavePlayer1.pop()
                                continue
                    else:
                        print("Zorg ervoor dat de boten niet op elkaar staan")
                        bootSavePlayer1.pop()
                        continue
                else:
                    print("Zorg ervoor dat de x coördinaten passen op het bord")
                    bootSavePlayer1.pop()
                    continue
            else:
                print("Zorg ervoor dat je maar 1 letter ingeeft")
                bootSavePlayer1.pop()
                continue
        else:
            print("Zorg ervoor dat de y coördinaten passen op het bord")
            bootSavePlayer1.pop()
            continue

def chooseMap():# schrijf opnieuwe
    map_number = random.randint(1,5)
    global boot2Save1Player2,boot2Save2Player2,boot2Save3Player2,boot2Save4Player2
    global boot3Save1Player2,boot3Save2Player2,boot3Save3Player2,boot3Save4Player2
    global boot4Save1Player2,boot4Save2Player2,boot4Save3Player2,boot4Save4Player2
    global boot6Save1Player2,boot6Save2Player2,boot6Save3Player2,boot6Save4Player2 
    if map_number == 1:
        boot2Save1Player2 = map1.boot2Save1Player2, boot2Save2Player2 = map1.boot2Save2Player2, boot2Save3Player2 = map1.boot2Save3Player2, boot2Save4Player2 = map1.boot2Save4Player2
        boot3Save1Player2 = map1.boot3Save1Player2, boot3Save2Player2 = map1.boot3Save2Player2, boot3Save3Player2 = map1.boot3Save3Player2
        boot4Save1Player2 = map1.boot4Save1Player2, boot4Save2Player2 = map1.boot4Save2Player2
        boot6Save1Player2 = map1.boot6Save1Player2
    if map_number == 2:
        boot2Save1Player2 = map2.boot2Save1Player2, boot2Save2Player2 = map2.boot2Save2Player2, boot2Save3Player2 = map2.boot2Save3Player2, boot2Save4Player2 = map2.boot2Save4Player2
        boot3Save1Player2 = map2.boot3Save1Player2, boot3Save2Player2 = map2.boot3Save2Player2, boot3Save3Player2 = map2.boot3Save3Player2
        boot4Save1Player2 = map2.boot4Save1Player2, boot4Save2Player2 = map2.boot4Save2Player2
        boot6Save1Player2 = map2.boot6Save1Player2
    if map_number == 3:
        boot2Save1Player2 = map3.boot2Save1Player2, boot2Save2Player2 = map3.boot2Save2Player2, boot2Save3Player2 = map3.boot2Save3Player2, boot2Save4Player2 = map3.boot2Save4Player2
        boot3Save1Player2 = map3.boot3Save1Player2, boot3Save2Player2 = map3.boot3Save2Player2, boot3Save3Player2 = map3.boot3Save3Player2
        boot4Save1Player2 = map3.boot4Save1Player2, boot4Save2Player2 = map3.boot4Save2Player2
        boot6Save1Player2 = map3.boot6Save1Player2
    if map_number == 4:
        boot2Save1Player2 = map4.boot2Save1Player2, boot2Save2Player2 = map4.boot2Save2Player2, boot2Save3Player2 = map4.boot2Save3Player2, boot2Save4Player2 = map4.boot2Save4Player2
        boot3Save1Player2 = map4.boot3Save1Player2, boot3Save2Player2 = map4.boot3Save2Player2, boot3Save3Player2 = map4.boot3Save3Player2
        boot4Save1Player2 = map4.boot4Save1Player2, boot4Save2Player2 = map4.boot4Save2Player2
        boot6Save1Player2 = map4.boot6Save1Player2
    if map_number == 5:
        boot2Save1Player2 = map5.boot2Save1Player2, boot2Save2Player2 = map5.boot2Save2Player2, boot2Save3Player2 = map5.boot2Save3Player2, boot2Save4Player2 = map5.boot2Save4Player2
        boot3Save1Player2 = map5.boot3Save1Player2, boot3Save2Player2 = map5.boot3Save2Player2, boot3Save3Player2 = map5.boot3Save3Player2
        boot4Save1Player2 = map5.boot4Save1Player2, boot4Save2Player2 = map5.boot4Save2Player2
        boot6Save1Player2 = map5.boot6Save1Player2
      
def shipPlaatser(shipCords):#intenet moet nog eens doorlezen!!!
    for coord in shipCords:
        row = coord[0]  # Extract the row letter
        col = int(coord[1:])  # Extract the column number
        # Update the corresponding cell with 'O'
        globals()[row + str(col)] = 'O'

def hitCeck(item, lists):#intenet help :( do understand fully 
    miss = 0
    for lst in lists:
        if item in lst:
            lst.remove(item)
            print("you hit")
        elif item not in lst:
            miss = miss + 1
    if miss == 3:
        print("you mist")
    return lists

def shipSchooter(player):
    global hitCeck
    shootloc = input(f"player {player} shoot: ")
    if player == 1:
        print("pp")
        hitCeck(shootloc,listOfAllPlayer2)
    elif player == 2:
        hitCeck(shootloc,listOfAllPlayer1)

def start1player():
    board()
    boot2(1)
    shipPlaatser(boot6Save1Player1)
    board()
    boot2(2)
    shipPlaatser(boot6Save1Player1)
    board()
    boot2(3)
    shipPlaatser(boot6Save3Player1)
    board()
    boot2(4)
    shipPlaatser(boot6Save4Player1)
    board()
    boot3(1)
    shipPlaatser(boot6Save1Player1)
    board()
    boot3(2)
    shipPlaatser(boot6Save1Player1)
    board()
    boot3(3)
    shipPlaatser(boot6Save3Player1)
    board()
    boot4(1)
    shipPlaatser(boot6Save1Player1)
    board()
    boot4(2)
    shipPlaatser(boot6Save1Player1)
    board()
    boot6(1)
    shipPlaatser(boot6Save1Player1)
    board()

def chooseMaptes():# schrijf opnieuwe
    map_number = 1
    global boot2Save1Player2,boot2Save2Player2,boot2Save3Player2,boot2Save4Player2
    global boot3Save1Player2,boot3Save2Player2,boot3Save3Player2
    global boot4Save1Player2,boot4Save2Player2
    global boot6Save1Player2
    if map_number == 1:
        boot2Save1Player2 = map1.boot2Save1Player2
        boot2Save2Player2 = map1.boot2Save2Player2
        boot2Save3Player2 = map1.boot2Save3Player2
        boot2Save4Player2 = map1.boot2Save4Player2
        boot3Save1Player2 = map1.boot3Save1Player2
        boot3Save2Player2 = map1.boot3Save2Player2
        boot3Save3Player2 = map1.boot3Save3Player2
        boot4Save1Player2 = map1.boot4Save1Player2
        boot4Save2Player2 = map1.boot4Save2Player2
        boot6Save1Player2 = map1.boot6Save1Player2

chooseMaptes()
shipSchooter(1)