#membuat contoh list 

nama = ["lisa","ningsi","liana","mery"]

#menampilkan list dengan perulangan 
for i in nama:
    print(i)

i = 0
while i < len(nama):
    print (nama[i])
    i += 1

#mengupdate

nama = ["lisa","ningsi","liana","mery"]
nama [0] = "intan"
print(nama)


#menambahkan

nama = ["lisa","ningsi","liana","mery"]
nama.append("anita")
print(nama)

nama.extend(["pira","ida"])
print(nama)

nama.insert(3, "uni")
print(nama)

#menghapus

nama = [ "lisa" , "ningsi" , "liana" , "mery" ]
nama.pop()
print (nama)

del  nama[ 1 ]
print (nama)

nama.remove( "lisa" )
print (nama)