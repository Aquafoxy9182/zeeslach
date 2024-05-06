lst = ["a1", "a2"]
same = True

def stop():
    global same
    if lst[0] == "a1":
        same = False

def prog():
    while same is True:
        print("PP")
        print(lst[0])
        stop()

prog()