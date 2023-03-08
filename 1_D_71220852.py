


def ganti_kata(kalimat,dicari,ganti):
    a=len(kalimat)

    for i in range(a):
        if kalimat[i]==dicari:
            kalimat[i]=ganti
    print("Kalimat baru:"," ".join(kalimat))
            

kalimat=input("Masukkan kalimat :").split()
dicari=input("Kata yang dicari :")
ganti=input("Diganti menjadi :")

ganti_kata(kalimat,dicari,ganti)
            
