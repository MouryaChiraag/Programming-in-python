# # burrito - 7, time - 9min, 2 burritos can be prepared at the same time.
# # fries - 4,
# # sodas - 2.50

# print("==========================================================================================")
# print("Burrito King")
# print("==========================================================================================")

# print('a) Orders\nb) Show sales report\nc) Updated Prices\nd) Exit')

# firstSelection = input('Enter your selection - a, b, c or d: ')

# match firstSelection:
#     case "a":   # order
#         print("1. Select the food item\n2. Enter amount\n3. Show the returned change")
#         orderSelection = input('Enter your selection - 1, 2 or 3: ')    
#         match orderSelection:
#             case 1:
#                 for _ in range(10):
#                     print('1. Burrito\n2. Fries\n3. Soda\n4. No more')
#                     foodSelection = input('Select the food item - 1, 2, 3 or 4')
#                     match foodSelection:
#                         case 1:
#                             noOfBurritos = input('How many burritos ($7) would you like to buy: ')
#                             priceOfBurritos = noOfBurritos * 7
#                             if timeOfBurritos < 2:
#                                 timeOfBurritos = 9
#                             else:
#                                 timeOfBurritos = 18
#                             if noOfBurritos == 1 or 2:
#                                 print(f'{timeOfBurritos} mins is required to prepare')
#                             else:    
#                                 print('please wait!')

                       
#                         case 2:
#                             noOfFries = input('How many serves of fries ($4) would you like to buy: ')
#                             print('Cooking fries, please be patient')
#                             if noOfFries <= 5:
#                                 timeOfFries = 8
#                             else:
#                                 timeOfFries = 16
#                             serveOfOneFries = 4
#                             batchOfFries = 5
#                             priceOfFries = noOfFries * serveOfOneFries
#                             remainingFries = batchOfFries-noOfFries
#                             print(f'{remainingFries}  serves of fries left for next order')
                           
#                         case 3:
#                             noOfSodas = input('How many sodas ($2.50) do you require: ')
#                             priceOfSodas = noOfSodas * 2.50

#                         case 4:
#                             #Total for 3 Burritos and 2 fries is $29.
#                             #Please enter money: 20
#                             #Sorry, that’s not enough to pay for order
#                             totalBillSelected = priceOfBurritos + priceOfFries
#                             print(f"Total for {noOfBurritos} Burritos and {noOfFries} Fries is {totalBillSelected}")
#                             for _ in range(10):
#                                 moneyHave = int(input("Please Enter Money : "))
#                                 if moneyHave < totalBillSelected:
#                                     print(f"Sorry, {moneyHave} is not enough to pay for order ")
#                                 else:
#                                   print(f"Change Returned ${moneyHave - totalBillSelected}")
#                                   print(f"Time Taken {timeOfBurritos + timeOfFries} minutes")
#                             break
                           
                               
               
#     case "b":   # show sales report
#         print(f"Unsold Serves Of Fries: {remainingFries}")
#         totalQuantity = noOfBurritos + noOfFries + noOfSodas
#         totalPrice = priceOfBurritos + priceOfFries + priceOfSodas
#         print(f"Total Sales:\nBurritos: {noOfBurritos}     ${priceOfBurritos}\nFries   : {noOfFries}     ${priceOfFries}
#         \nSodaa   : {noOfSodas}     ${priceOfSodas}\n-------------------------\n         {totalQuantity}     ${totalPrice}")
#         break
   
#     case "c":   # Updated Prices
#         pass
   
#     case "d":   # Exit
#         print("Bye Bye")
#         break
   
#     case default:
#         print("Invalid input")

print("==========================================================================================")
print("Burrito King")
print("==========================================================================================")

print('a) Orders\nb) Show sales report\nc) Updated Prices\nd) Exit')

remainingFries = 0  # Initialize remaining fries

while True:
    firstSelection = input('Enter your selection - a, b, c or d: ')

    if firstSelection == "a":   # order
        print("1. Select the food item\n2. Enter amount\n3. Show the returned change")
        orderSelection = input('Enter your selection - 1, 2 or 3: ')
        if orderSelection == "1":
            for _ in range(10):
                print('1. Burrito\n2. Fries\n3. Soda\n4. No more')
                foodSelection = input('Select the food item - 1, 2, 3 or 4: ')
                if foodSelection == "1":
                    noOfBurritos = int(input('How many burritos ($7) would you like to buy: '))
                    priceOfBurritos = noOfBurritos * 7
                    timeOfBurritos = 9 if noOfBurritos <= 2 else 18
                    print(f'{timeOfBurritos} mins is required to prepare')

                elif foodSelection == "2":
                    noOfFries = int(input('How many serves of fries ($4) would you like to buy: '))
                    print('Cooking fries, please be patient')
                    if noOfFries <= 5:
                        timeOfFries = 8
                    else:
                        timeOfFries = 16
                    serveOfOneFries = 4
                    batchOfFries = 5
                    priceOfFries = noOfFries * serveOfOneFries
                    remainingFries += batchOfFries - noOfFries
                    print(f'{remainingFries} serves of fries left for next order')

                elif foodSelection == "3":
                    noOfSodas = int(input('How many sodas ($2.50) do you require: '))
                    priceOfSodas = noOfSodas * 2.50

                elif foodSelection == "4":
                    totalBillSelected = priceOfBurritos + priceOfFries
                    print(f"Total for {noOfBurritos} Burritos and {noOfFries} Fries is {totalBillSelected}")
                    for _ in range(2):
                        moneyHave = int(input("Please Enter Money : "))
                        if moneyHave < totalBillSelected:
                            print(f"Sorry, {moneyHave} is not enough to pay for order ")
                        else:
                            print(f"Change Returned ${moneyHave - totalBillSelected}")
                            print(f"Time Taken {timeOfBurritos + timeOfFries} minutes")
                            break


    elif firstSelection == "b":   # show sales report
        totalQuantity = noOfBurritos + noOfFries + noOfSodas
        totalPrice = priceOfBurritos + priceOfFries + priceOfSodas
        print(f"Unsold Serves Of Fries: {remainingFries}")
        print(f"Total Sales:\nBurritos: {noOfBurritos}     ${priceOfBurritos}\nFries   : {noOfFries}     ${priceOfFries}\nSoda   : {noOfSodas}     ${priceOfSodas}\n-------------------------\n         {totalQuantity}     ${totalPrice}")
        break

    elif firstSelection == "c":   # Updated Prices
        pass

    elif firstSelection == "d":   # Exit
        print("Bye Bye")
        break

    else:
        print("Invalid input")
