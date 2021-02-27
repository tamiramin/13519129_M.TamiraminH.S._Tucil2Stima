import Topo as tp
# M.Tamiramin H.S. 13519129
# Topological Sort pendekatan Decrease and Conquer 
# diasumsikan masukan dari .txt tidak melebihi 30 baris 


Solusi = []
Neff = 0 
tempid = []

tp.bacafile()                                                 # membaca file dari file mahasiswa.txt
for j in range(8): 
# diulangi hingga delapan kali dikarenakan terdapat delapan semester 
    for i in range(len(tp.nodelist)):
    # pengulangan untuk memproses array of Node yang sisa setelah Node yang memiliki derajat masuk 0 dihapus hal ini merupakan metode decrease 
    # and conquer , yaitu hanya salah satu array yang diposes kembali dan tidak melakukan combine solusi.
        if tp.nodelist[i]["Npred"] == 0 and tp.nodelist[i]["Id"] != '' :
            tempid.append(tp.nodelist[i]["Id"])                 
        # memasukan Node yang memiliki derajat masuk 0  dan memasukan kepada array  temp id yang saat ini juga array dari node dibagi menjadi 2 
        # array pertama adalah array node yang tidak memiliki derajat masuk dan yang satu lagi memiliki, penyimpanan ini bersifat sementara
        # yang nantinya akan dimasukkan ke dalam array Solusi
    
    for k in range(len(tempid)):
        tp.delete(tempid[k])
        # pemrosesan untuk menghilangkan Node yang tidak memiliki derajat masuk pada array of Node
    if tempid != [] :
        Solusi.append(tempid)
        # Solusi merupakan array tetap yang setiap indeksnya bernilai mata kuliah yang dapat diambil dari semester 
        Neff += 1 
        # Neff merupakan jumlah indeks efektif yang digunakan pada Array of node pada nodelist , karena nodelist diinisiasikan sepanjang 20 
    tempid = [] 
    # mengosongkan kembali array of solusi yang berseifat sementara agar dapat menerima solusi baru di semester berikutnya
for i in range(Neff):
    if(i < Neff-1) :
        print("Semester ", i+1 , "    :", ', '.join(Solusi[i]))
    else :
        print("Semester ", i+1 , "    :", ', '.join(Solusi[i]), end=".")


