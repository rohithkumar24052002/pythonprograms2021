number1 = str(input("enter the number:"))
list_of_numbers = list(str(number1))
print('the list is:' ,list_of_numbers)
list_of_numbers.reverse()
print('updated list:',list_of_numbers)
number2 = ""
for i in list_of_numbers:
    list_of_numbers+= str(i) + " "
number2 = number2[:-1]
print (number2)