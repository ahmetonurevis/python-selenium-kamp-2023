# SORU1) Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

#Python’da veri tipleri şu şekildedir;

#String veri tipleri => String değerler tek tırnak işareti veya çift tırnak işareti içinde ifade edilirken, bir değişkene string değer atama; değişken adı ve ardından eşittir işareti ile yapılır.

#Numerik veri tipleri => Python’da üç tür numerik sayısal veri tipi bulunmakla birlikte; Int negatif ve pozitif tam sayıları, Float negatif ve pozitif ondalıklı sayıları temsil ederken, Complex sayılar ise daha çok ileri düzey matematik işlemlerinde kullanılmaktadır.

#Sequence veri tipleri => List birden fazla veri dizisini tek bir tipte birleştirmeyi sağlarken içinde string, int ve float değerler barındırabilir. Range bir fonksiyon olarak çalışmakla birlikte genellikle döngülerin içerisinde kullanılır. Tuple ise parantez ile çalışan, dizi oluşturan bir yapıdır ve sıralı bir biçimde oluşturulmaktadır.

#Set veri tipleri => Kümeler birden çok öğeyi tek bir değişken içerisinde tutmak için kullanılır ve süslü parantez ile yazılır. Set ve Frozenset olarak ikiye ayrılır. 

#Mantıksal veri tipleri  => Bool yapısı doğru veya yanlış (true/false) mantığı ile çalışır.

#Binary veri tipleri => Bytes verilmiş olan boyutta ve girilen verilerle başlatılan değişmez bir bayt nesnesini kendi içerisinde döndürürken, Bytearray byte veri tipinde oluşturulan veriler üzerinde değişiklik için yapmakta kullanılır.  Memoryview ise Python’da bellek durumunu görüntülemek için kullanılır.



# SORU2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# String veri tipi olarak kurslarım, tüm kurslar, kariyer, sık sorulan sorular, kullanım koşulları ve gizlilik politikasını örnek gösterebiliriz.
# List veri tipine kategori ve eğitmenleri örnek verebiliriz. 
# Eğitim %30-%60 tamamlandı ise integer veri tipine örnektir

BitirVeDevamEt= True
#eğer bitirdi ise butona bastığında tamamlandığını ifade eder.

if BitirVeDevamEt == False:
    print("Bitir ve devam et tamamlanma butonu olduğu için dairenin içi mavi renkle ve beyaz tik işareti ile dolsun")

else:
    print("Tamamlanmadığı için dairenin içinin yarısı mavi yarısı beyaz renk ile dolsun")