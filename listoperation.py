word = str(input("enter the word:"))
list_of_letters = list(word)
print('the list is:' ,list_of_letters)
list_of_letters.reverse()
print('updated list:',list_of_letters)
list_of_objects =" "
for i in list_of_letters:
    list_of_objects += str(i) + " "
list_of_objects = list_of_objects[:-1]
print (list_of_objects)

