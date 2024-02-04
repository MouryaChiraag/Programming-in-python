# if vacation:
#weekdays - 1-5 ; 10:00 AM
#weekends  - 6-7 ; "OFF"

#if not vacation:
#weekdays - 1-5 ; 7:00 AM
#weekends - 6-7 ; 10:00 AM

# def alarm(day, vacation):
#     weekdays = [1,2,3,4,5]
#     weekend = [6,7]
#     if day in weekdays and vacation == True:
#         return "10:00 AM"
#     elif day in weekdays and vacation == False:
#         return "07:00 AM"
#     elif day in weekend and vacation == True:
#         return "OFF"
#     else:
#         return "10:00 AM"

# alarm_day = int(input("Enter the Day : "))
# alarm_vacation = bool(input("Enter if it is Vaction or Not : "))
# print(alarm(alarm_day, alarm_vacation))

# def alarm(day, vacation):
#     weekdays = [1,2,3,4,5]
#     weekends = [6,7]
#     if vacation :
#         if day in weekdays:
#             return "10 : 00 AM"
#         else:
#             return "OFF"
#     else:
#         if day in weekdays:
#             return "07:00 AM"
#         else:
#             return "10:00 AM"
        
# alarm_day = int(input("Enter the Day : "))
# alarm_vacation = input("Enter if it is Vaction or Not : ")
# print(alarm(alarm_day, alarm_vacation))

def alarm(day, vacation):
    weekdays = [1, 2, 3, 4, 5]
    weekends = [6, 7]
    
    if vacation:
        if day in weekdays:
            return "10:00 AM"
        else:
            return "OFF"
    else:
        if day in weekdays:
            return "07:00 AM"
        else:
            return "10:00 AM"

alarm_day = int(input("Enter the Day: "))
alarm_vacation = input("Enter if it is Vacation or Not (True/False): ").lower() == "true"
print(alarm(alarm_day, alarm_vacation))
