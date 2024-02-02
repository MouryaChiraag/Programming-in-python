list_1 = [9,4,0,6,2]
for i in range (len(list_1) - 1) :
    for j in range (len(list_1) - 1) :
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
        else:
            j+= 1
print(list_1)