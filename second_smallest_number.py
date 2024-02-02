list_1 = [3,5,1,9,4]  #create a list
for i in range(0,len(list_1) - 1) :  #outer loop
    for j in range(0, len(list_1) - 1):  #inner loop
        if list_1[j] > list_1[j + 1]:  #comparing 2 var
            list_1[j], list_1[j+1] = list_1[j + 1], list_1[j]  # swap
        else:
            j = j + 1  #increase the pointer number
print(list_1[1])