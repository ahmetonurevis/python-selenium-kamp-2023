ogrenciler = ["Ahmet Evis", "Hakan Soyer", "Alperen Özdemir", "Oğuzhan Demirci"]

print(ogrenciler)

# Öğrenci Ekleme
ogrenciler.append("Salman Kerim")
print(ogrenciler)

# Öğrenci Silme
ogrenciler.remove('Alperen Özdemir')
print(ogrenciler)

# Listeye Çoklu Ekleme

ogrenciler.extend(["Bahar Karabulut", "Oğuzhan Tuna", "Kerem Genbay"])
print(ogrenciler)

# Tek Tek Yazdırma
for i in ogrenciler:
     print(i)

#Numara Öğrenme
student=input("Numarasını öğrenmek istediğiniz kişinin ad-soyad bilgisini giriniz: ")
print(ogrenciler.index(student))

ogrSil = int(input("Kaç tane öğrenci silmek istiyorsunuz?: "))
while i < ogrSil:
     ogrenciler.pop()
     i +=1
print(ogrenciler)




