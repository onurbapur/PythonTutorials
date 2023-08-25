x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Bir değişkenin veri türünü belirtmek istiyorsanız, bu şekilde yapılabilir.

x = input('1. sayıyı giriniz: ')  # input metodu kullanıcıdan girdi (input) alır
y = input('2. sayıyı giriniz: ')  # Bunları str olarak alacaktır.

toplam = int(x) + int(y)    # str olan değerleri int yapıp toplayacaktır

print(toplam)
print(type(x)) # x -- str casting yaparken atama yapılmadığı sürece değişken tipi değişmez

x = int(x)

print(type(x))