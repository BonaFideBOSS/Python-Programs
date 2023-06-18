def unmerge(level,target):
    tree = 1
    while target > level:
        target = target - 1
        tree = tree*2
        amount = str(target)*tree
        print(f"{target} : {len(amount)}")


def merge(level,quantity):
    remains = {}
    while quantity > 0:
        print(f"Lvl {level} : {quantity} | remains: {remains}")
        remainder = divmod(quantity,2)[1]
        if remainder > 0:
            remains[f"Lvl {level}"] = divmod(quantity,2)[1]
        quantity = quantity // 2
        level = level + 1
            

# How many items of level N is needed to reach target level
unmerge(1,6)

# possible merges using item of level N of given quantity
merge(2,30)
