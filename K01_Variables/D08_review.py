print()

website = "https://www.sadikturan.com"
course = "Python kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 'course' karakter dizisinde kaç karakter bulunmaktadır
lengthOfCourse = str(len(course))
print("'course' karakter dizisinde " + lengthOfCourse + " karakter bulunmaktadır.")

#2 'website' içinden 'www' karakterlerini alın
www = website[8:11]
print("'website' içinden 'www' karakterleri: " + www)

#3 'website' içinden 'com' karakterlerini alın
com = website[23:]
print("'website' içinden 'www' karakterleri: " + com)

#4 'course' içindeki ilk ve son 15 karakter
ilk15 = course[:15]
son15 = course[-15:]
print("'course2' içinde ilk 15 karakter: " + ilk15)
print("'course2' içinde son 15 karakter: " + son15)

#5 'course' ifadesindeki karakterleri tersten yazdırın
print()
print(course[::-1])


name, surname, age, job = "Onur", "Bapur", 34, "Mühendis"
#6 'Benim adım Onur Bapur, Yaşım 34 ve mesleğim Mühendis.'  yazdırın
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

helloWorld = "Hello world"
#7 'helloWorld' karakter dizisindeki 'w' harfini 'W' ile değiştirin
helloWorld = helloWorld[:6] + "W" + helloWorld[7:]
print(helloWorld)

#8 'abc' ifadesini 3 defa yan yana yazdırın
print("abc" * 3)


print()