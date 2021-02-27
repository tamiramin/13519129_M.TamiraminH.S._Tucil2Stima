nodelist = [ { "Id" : "", "Npred" : -1, "prereq" : [] } for j in range(30)]

# M.Tamiramin H.S. 13519129 
# diasumsikan masukan dari .txt tidak melebihi 30 baris


# data dictionay yang dipakai untuk menyimpaj node pada graf 
# dict{  
#   "id" : "namamatkul"
#   "Npred" : 0
#   "prereq" : [] 
# }

def bacafile():  # membava file dari file mata kuliah.txt dan memasukan nilai nya ke dalam dictionary
    f = open("../test/matakuliah.txt", "r") 
    n = 0 
    for row in f :
        kolom = row.split(",")
        clear(kolom)
        makenode(n,kolom)
        n += 1 
    f.close()

def makenode(n,kolom) :   # membuat node dengan memasukannya ke dalam dictionary 
    if len(kolom) > 1 :
        nodelist[n] = { "Id" : kolom[0], "Npred" : len(kolom)-1, "prereq" : kolom[1:len(kolom)] } 
    else :
         nodelist[n] = { "Id" : kolom[0], "Npred" : len(kolom)-1, "prereq" : [] } 

def clear(kolom):    # membersihkan string dari spasi dan newline 
    for i in range(1,len(kolom)-1):
        kolom[i] = kolom[i].replace(" ","")
    kolom[len(kolom)-1] = kolom[len(kolom)-1].replace(" ","")
    kolom[len(kolom)-1] = kolom[len(kolom)-1].replace(".","")
    kolom[len(kolom)-1] = kolom[len(kolom)-1].replace("\n","")


def delete(id) : # prosedur delete node sesuai dengan id 
    for i in range(0,len(nodelist)) :  #mencari pada list of node yang memiliki id == id 
        if (nodelist[i]["Id"] == id) and nodelist[i]['Npred'] == 0 :
            nodelist[i] = { "Id" : "", "Npred" : -1, "prereq" : [] }  
    for i in range(0,len(nodelist)):
        arr = nodelist[i]["prereq"]
        if  iselmt(id,i,arr) :
            nodelist[i]["prereq"].remove(id)
            nodelist[i]['Npred'] -= 1

def iselmt(id,i,arr) : # mencek apakah di dalam prerequisite terdapat matakuliah dengan idnya adalah id, jika ada kembalikan true dan sebaliknya
    n = len(arr)
    for j in range(n) :
        if arr[j] == id :
            return True
    return False  









