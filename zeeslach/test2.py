#=============================================================boot4groot===============================================================#
def drieBootlocatieVraag(bootcountvier):
    global abc, drieBootlocatieVraagTrue, middelDrie, middelDrieLetter
    while drieBootlocatieVraagTrue is True:
        vierBootlocatieSavePlayer1.clear()
        print("plaats drie boot", bootcountvier ,"drie vakjes dus")

#=============================================================eersteCord===============================================================#
        vierBootlocatie1 = input("geeft cord 1: ") 
        onlyleter1 = re.sub("[^a-zA-Z]", "", vierBootlocatie1)
        onlyNumber1 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", vierBootlocatie1)
        if onlyleter1 in abc:
            if len(onlyleter1) == 1:
                if len(onlyNumber1) == 1 or onlyNumber1 == "10":
                    if vierBootlocatie1 not in drieBootlocatieSavePlayer1 and vierBootlocatie1 not in drieBootlocatieSavePlayer2 and vierBootlocatie1 not in kleineBootlocatieSavePlayer1 and vierBootlocatie1 not in kleineBootlocatieSavePlayer2:
                        vierBootlocatieSavePlayer1.append(vierBootlocatie1)

                        if bootcountvier == 1:
                            vierBootlocatieSave1Player1.append(vierBootlocatie1)
                        elif bootcountvier == 2:
                            if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0]: 
                                kleineBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave2Player1.append(vierBootlocatie1)
                        elif bootcountvier == 3:
                            if vierBootlocatie1 == vierBootlocatieSave1Player1[0] or vierBootlocatie1 == vierBootlocatieSave2Player1[0]: 
                                vierBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                kleineBootlocatieSave3Player1.append(vierBootlocatie1)
                        elif bootcountvier == 4:
                            if vierBootlocatie1 == vierBootlocatieSave1Player1[0] or vierBootlocatie1 == vierBootlocatieSave2Player1[0] or vierBootlocatie1 == vierBootlocatieSave3Player1[0]: 
                                vierBootlocatieSavePlayer1.clear()
                                continue
                            else:
                                vierBootlocatieSave4Player1.append(vierBootlocatie1)
                    else:
                        
                        print("zorg er voor dat je niet 2 keer de zelfde cordinaten gvierBootlocatieSavePlayer1.clear()ebruikt<3")
                        continue
#=============================================================tweedeCord===============================================================#
                    vierBootlocatie = input("geeft cord 2: ")
                    onlyleter2 = re.sub("[^a-zA-Z]", "", vierBootlocatie)
                    onlyNumber2 = re.sub("[^1-2-3-5-6-7-8-9-10]", "", vierBootlocatie)
                    if onlyleter2 in abc:
                        if len(onlyleter2) == 1:
                            if len(onlyNumber2) == 1 or onlyNumber2 == "10":
                                if onlyleter1 == onlyleter2:
                                    if int(onlyNumber2) == int(onlyNumber1) + 2 or int(onlyNumber2) == int(onlyNumber1) - 2:
                                        if vierBootlocatieSave1Player1 not in vierBootlocatieSavePlayer1 and vierBootlocatieSave1Player1 not in vierBootlocatieSavePlayer2 and vierBootlocatieSave1Player1 not in kleineBootlocatieSavePlayer1 and vierBootlocatieSave1Player1 not in kleineBootlocatieSavePlayer2:
                                            vierBootlocatieSavePlayer1.append(vierBootlocatieSave1Player1)
                                            print (vierBootlocatieSavePlayer1)
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 2 or abc.index(onlyleter2) == abc.index(onlyleter1) - 2 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountvier == 1:
                                                    print(vierBootlocatie1)
                                                    vierBootlocatieSave1Player1.append(vierBootlocatie1)
                                                    kleineBootlocatieSavePlayer1.append(vierBootlocatie)
                                                elif bootcountvier == 2:
                                                        if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            vierBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            vierBootlocatieSave2Player1.append(vierBootlocatie1)
                                                elif bootcountvier == 3:
                                                    if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave3Player1.append(vierBootlocatie1)
                                                elif bootcountvier == 4:
                                                    if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave3Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave4Player1.append(vierBootlocatie1)

                                                vierBootlocatieSavePlayer1.append(vierBootlocatie1)
                                                middelDrieNumber = int(onlyNumber2) - 1
                                                index = abc.index(onlyleter2)  # Get the index of onlyleter2 in the abc list
                                                preceding_letter = abc[index]  # Get the preceding letter
                                                middelDrie = preceding_letter + str(middelDrieNumber)
                                                vierBootlocatieSavePlayer1.append(middelDrie)
                                                drieBootlocatieVraagTrue = False
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
                                        if vierBootlocatieSave1Player1 not in vierBootlocatieSavePlayer1 and vierBootlocatieSave1Player1 not in vierBootlocatieSavePlayer2:
                                            vierBootlocatieSavePlayer1.append(vierBootlocatieSave1Player1)
                                            print (vierBootlocatieSavePlayer1)
            
                                            if  abc.index(onlyleter2) == abc.index(onlyleter1) + 2 or abc.index(onlyleter2) == abc.index(onlyleter1) - 2 or abc.index(onlyleter2) == abc.index(onlyleter1):
                                                if bootcountvier == 1:
                                                    print("1 work pleas")
                                                    vierBootlocatieSave1Player1.append(vierBootlocatieSave1Player1)
                                                elif bootcountvier == 2:
                                                        if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1]:
                                                            print("zorg ervoor dat de booten niet op elkaarstaan")
                                                            vierBootlocatieSavePlayer1.clear()
                                                            continue
                                                        else:
                                                            vierBootlocatieSave2Player1.append(vierBootlocatieSave1Player1)
                                                elif bootcountvier == 3:
                                                    if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave3Player1.append(vierBootlocatieSave1Player1)
                                                elif bootcountvier == 4:
                                                    if vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave3Player1[0] or vierBootlocatieSave1Player1 == vierBootlocatieSave1Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave2Player1[1] or vierBootlocatieSave1Player1 == vierBootlocatieSave3Player1[1]:
                                                        print("zorg ervoor dat de booten niet op elkaarstaan")
                                                        vierBootlocatieSavePlayer1.clear()
                                                        continue
                                                    else:
                                                        vierBootlocatieSave4Player1.append(vierBootlocatieSave1Player1) 

                                                vierBootlocatieSavePlayer1.append(vierBootlocatieSave1Player1)
                                                middelDrieNumber = int(onlyNumber2) 
                                                index = abc.index(onlyleter2)  
                                                preceding_letter = abc[index - 1] 
                                                middelDrie = preceding_letter + str(middelDrieNumber)
                                                vierBootlocatieSavePlayer1.append(middelDrie)
                                                drieBootlocatieVraagTrue = False
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