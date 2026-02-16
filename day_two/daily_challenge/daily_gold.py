ligne_2 = "   |:H:a:p:p:y:|   "
ligne_3 = "   |           |   "
ligne_4 = " __|___________|__ "
ligne_5 = "|^^^^^^^^^^^^^^^^^|"
ligne_6 = "|:B:i:r:t:h:d:a:y:|"
ligne_7 = "|                 |"
ligne_8 = "~~~~~~~~~~~~~~~~~~~"

birthday_date = input('When is your birthday ? DD//MM/YYYY')
lst = birthday_date.split("//")
if int(lst[1]) > 2:
    age = 2026 - int(lst[2]) -1
elif int(lst[1]) ==2:
    if int(lst[0])<=16:
        age = 2026 - int(lst[2])
    else:
        age = 2026 - int(lst[2]) -1
elif int(lst[1]) ==1:
    age = 2026 - int(lst[2])
num = age%10
candles = 'i'*num
prefix = "    _"
sufix = "_   "
middle1 ="_"*((9 - num)//2)
middle2 = "_"*(9 - len(middle1) - num)
ligne_1 = prefix+middle1+candles+middle2+sufix
print(ligne_1)
print(ligne_2)
print(ligne_3)
print(ligne_4)
print(ligne_5)
print(ligne_6)
print(ligne_7)
print(ligne_8)