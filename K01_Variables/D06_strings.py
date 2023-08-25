name = 'Sadık' # bu 5 elemanlı bir karakter dizisi
surname = 'Turan'
age = 36

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.'

print(greeting)

lengthOftext = len(greeting) # int olarak metnin karakter uzunluğunu verir.

print(greeting[4])  #textin indek 4teki yani 5. karakterini yazdırır: 'a'

# metnin son karakterini yazmak istersem:

print(greeting[len(greeting)-1])
print(greeting[lengthOftext-1])
print(greeting[-1])

#   Aradaki bir kısım kelimeleri ya da karakterleri yazmak istersem

print(greeting[3:7])

print(greeting[8:])

print(greeting[:15]) # ilk 15 karakteri alır

print(greeting[3:40:2]) # bir karakter atlayarak alır