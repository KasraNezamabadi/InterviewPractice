my_list = [1, 2, 3, 4]
set1 = set(list)
set2 = {1, 2, 5}

set2.add(7)
set1.remove(2)

set1.issubset()
set1.isdisjoint()


setU = set1 | set2
setI = set1 & set2
setD = set1 - set2

if key in set1:
    print(key)

for item in set1:
    print(item)