#=============================================================imports==================================================================#
import re

#=============================================================variable=================================================================#
abc = ["a","b","c","d","e","f","g","h","i","j"]

kleineBootlocatieSavePlayer1 = []
kleineBootlocatieSavePlayer2 = []
kleineBootlocatieVraagTrue = True

#=============================================================functions=================================================================#
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

#=============================================================program==================================================================#
kleineBootlocatieVraag()