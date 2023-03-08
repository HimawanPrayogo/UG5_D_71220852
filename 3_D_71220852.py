import math



while True:
    awal=input("Masukkan jarak awal (dalam meter):").lower()

    if awal=="stop" or awal=="berhenti":
        print("Program dihentikan")
        break
    else:
        awal=int(awal)

        sudut5=int(input("Masukkan sudut elevasi pada menit ke-5 (salam derajat):"))
        sudut6=int(input("Masukkan sudut elevasi pada menit ke-6 (salam derajat):"))

        radian1=math.radians(sudut5)
        radian2=math.radians(sudut6)

        tinggiawal=awal*(math.tan(radian1))
        jarakakhir=awal*((math.tan(radian2)) - (math.tan(radian1)))
        selisihtinggi=jarakakhir*(math.tan(radian2))

        print(f"Ketinggian drone pada menit ke -5 adalah {tinggiawal:.2f} meter")
        print(f"Selisih ketinggian drone saat menit ke -5 dan ke -6 adalah {selisihtinggi:.2f} meter")
        
        print()
    
    
