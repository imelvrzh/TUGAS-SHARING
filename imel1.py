print("")
print("HITUNG SELISIH ASCII")
print("")

jumlah = input("Ada berapa kata : ")
jumlah = int(jumlah)

data = []
for i in range(jumlah) :
    kata = input(f"Masukkan kata ke-{i+1} : ")
    data.append(kata)
    
for j in data :
    print("")
    print("Hasil : ")
    for index, k in enumerate (j) :
        if index == len(j) - 1 :
            break
        else :
            if ord(j[index]) > ord(j[index+1]):
                selisih = ord(j[index]) - ord(j[index+1])
                print(f"{j[index]} lebih dari {j[index+1]}, selisihnya ialah {selisih}")
                
            elif ord(j[index]) < ord(j[index+1]):
                selisih = ord(j[index]) - ord(j[index+1])
                selisih *= -1
                print(f"{j[index]} lebih dari {j[index+1]}, selisihnya ialah {selisih}")
                
            elif ord(j[index]) == ord(j[index+1]):
                selisih = 0
                print(f"{j[index]} lebih dari {j[index+1]}, selisihnya ialah {selisih}")