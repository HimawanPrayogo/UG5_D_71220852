sol=0
sur=0
jog=0
mag=0

def hitung_mobil(sol,sur,jog,mag):
    while True:
        asal=input('masukkan asal mobil (ketik "done" untuk keluar):').lower()
        if asal=="solo":
            sol+=1

        elif asal=="surabaya":
            sur+=1

        elif asal=="jogja":
            jog+=1

        elif asal=="magelang":
            mag+=1

        elif asal=="done":
            print("Jumlah Mobil Solo\t:",sol)
            print("Jumlah Mobil Surabaya\t:",sur)
            print("Jumlah Mobil Jogja\t:",jog)
            print("Jumlah Mobil Magelang\t:",mag)
            break

hitung_mobil(sol,sur,jog,mag)        

        
