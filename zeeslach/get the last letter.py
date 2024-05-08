name = input("what is your name: ")
namelengt = len(name)

print (namelengt)
for i in name:
    print(name[namelengt-1], end ="")
    namelengt = namelengt - 1

