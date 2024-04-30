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

abc = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

player2 = bool

kleineBootlocatieVraagTrue = True
kleineBootlocatieSavePlayer1 = []
kleineBootlocatieSavePlayer2 = []

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
    global kleineBootlocatieVraagTrue
    while kleineBootlocatieVraagTrue is True:
        print("plaats kleine boot twee vakjes dus")
        kleineBootlocatie = input("geeft cord 1: ")
        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
            kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
        kleineBootlocatie = input("geeft cord 2: ")
        if kleineBootlocatie not in kleineBootlocatieSavePlayer1 and kleineBootlocatie not in kleineBootlocatieSavePlayer2:
                onlyLeter = re.sub("[^a-zA-Z]", "", kleineBootlocatie)
                
                kleineBootlocatieSavePlayer1.append(kleineBootlocatie)
                kleineBootlocatieVraagTrue == False
        else:
            print("fout brobeer opnieuw")
            continue

def kleinebootPlaatser():
    kleineBootlocatie = input("plaat kleine boot (2 vakjes naar boven: ")

    if kleineBootlocatie == "a1" or "a2" or "a3" or "a4":
        print("foute cordinaten")

#=============================================================program==================================================================#
player_select()

if player2 == False:
    board()
    kleineBootlocatieVraag()

