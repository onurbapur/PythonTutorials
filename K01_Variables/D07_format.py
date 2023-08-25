name ='Onur'
surname = 'Bapur'
age = 36

print('My name is {} {}'.format(name, surname))     # Onur Bapur
print('My name is {1} {0}'.format(name, surname))   # Bapur Onur
print('My name is {s} {n}'.format(n=name, s=surname))   # Bapur Onur

print("My name is {} {} and I'am {} years old.".format(name, surname, 36))
print("My name is {} {} and I'am {} years old.".format(name, surname, '36'))
print("My name is {} {} and I'am {} years old.".format(name, surname, age))

result = 200 / 700
print("The  result is {}".format(result))

# virgülden sonrasını uyarlamak için
print("The  result is {r:1.3}".format(r=result))
print("The  result is {r:1.9}".format(r=result))

# f string kullanımı
print(f"My name is {name} {surname} and I'am {age} years old.")

word = "12345" * 5
print(word)