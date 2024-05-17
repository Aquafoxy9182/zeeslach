# Example lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

def remove_item_from_lists(item, lists):
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

all_lists = [list1, list2, list3]

item_to_remove = 10
all_lists = remove_item_from_lists(item_to_remove, all_lists)

print(all_lists)