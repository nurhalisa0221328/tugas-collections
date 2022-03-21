#membuat contoh tuple
buah = ("nanas", "apel", "durian", "pisang", "sawo")

#menampilkan tuple dengan perulangan
for i in buah :
   print(i)

a = 0
while a < len(buah):
   print(buah[a])
   a += 1

buah = list(buah)

#mengupdate salah satu tuple
buah [2] = "rambutan"
print(buah)

#menghapus salah satu tuple
buah.pop()
print(buah) 

buah.remove ("apel")
print(buah)

del buah [0:2]
print(buah)

#menambahkan tuple
buah.append ("ceri")
print(buah)

buah. extend(["semangka", "langsat"])
print(buah)

buah.insert(3, "anggur")
print(buah)