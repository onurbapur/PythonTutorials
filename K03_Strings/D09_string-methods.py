# str.upper() metodu str ifadesini büyük harflere dönüştürür.
message = 'Hello There. My name is Onur Bapur'
message = message.upper()
print(message) 

# str.lower() metodu str ifadesini büyük harflere dönüştürür.
message = 'Hello There. My name is Onur Bapur'
message = message.lower()
print(message) 

# str.title() metodu str ifadesini her kelimesinin ilk harfi büyük harfe dönüştürür.
message = 'Hello There. My name is Onur Bapur'
message = message.title()
print(message) 

# str.capitalize() metodu str ifadesinin sadece ilk harfi büyük harfe dönüştürür.
message = 'Hello There. My name is Onur Bapur'
message = message.capitalize()
print(message) 

# str.strip() metodu ifadenin başındaki ve sonundaki boşlukları alır
str1 = " Onur Bapur "
strNew = str1.strip()
print(strNew)

# str.split() metodu ifadeyi boşluklara göre böler ve dizi olarak döndürür.
# str.split("karakter") metodu ifadeyi karaktere göre böler ve dizi olarak döndürür.
message = 'Hello There. My name is Onur Bapur'
message = message.split()
print(message)

# "karakter".join(dizi)  dizideki elemanları aralara karakter koyarak birleştirir
print("*-* ".join(message))

# str.find("ifade") metodu str içinde ifade varsa başladığı indexi verir
# str.startswith("ifade") str ifade ile başlar mı boolean döner
# str.endswith("ifade") str ifade ile sonlanır mı boolean döner


# str.replace(ifade1, ifade2) str de ifade1 i ifade2 ile dönüştürür
'''
str.replace(a1,a2)
   .replace(b1,b2)
   .replace(c1,c2)
'''

name = "Onur Bapur"
print(name.center(50,"^"))  # 5 karakterlik alanda ortaya name yazar sağ sol kısmı da ^ ile doldurur.