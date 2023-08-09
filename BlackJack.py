import module
import random
import pyfiglet
from colored import fg

#colorfg
blue1 = fg('light_sky_blue_3a')   
blue2 =  fg('light_sky_blue_3b')   
blue3 = fg('sky_blue_2')        
blue4 = fg('chartreuse_2b')    

deep_pink_4c = fg('deep_pink_4c')
medium_violet_red = fg('medium_violet_red')
darkviolet = fg('dark_violet_1b')
purple = fg('purple_1b')

red = fg('red_3a')
green = fg('green_1')
gold = fg('light_goldenrod_3')

kartu=module.membuatkartu()

cekmenu=True
option=module.begin()
if option=='register' :
    option=module.access(option)
    data=module.access(option)
else:
    data=module.access(option)
chips=data[2]

while (cekmenu==True):
    main=module.fungsimenu()
    
    while (main=="ya"):
        pemain=[]
        komputer=[]
        jumlahkartuas=0
        kartuasbernilai11=0
        poinpemain=0
        poinkomputer=0
        bet = int(input("ingin bertaruh berapa? "))

        pemain.append(module.membagikartu(kartu))
        komputer.append(module.membagikartu(kartu))
        pemain.append(module.membagikartu(kartu))
        komputer.append(module.membagikartu(kartu))

        jumlahkartuas=jumlahkartuas+module.mengecekkartuas(pemain[0])
        jumlahkartuas=jumlahkartuas+module.mengecekkartuas(pemain[1])

        poinpemain=module.menghitungkartu(pemain[0]) + module.menghitungkartu(pemain[1])
        poinkomputer=module.menghitungkartu(komputer[0]) + module.menghitungkartu(komputer[1])

        print()
        print("ini kartu yang kamu dapat",pemain)
        cek=module.menghitungkartuas(jumlahkartuas)
        poinpemain=poinpemain+cek[0]
        kartuasbernilai11=cek[1]
        komputer1=komputer[0]
        print()
        print()
        print("ini jumlah kartu kamu sekarang",poinpemain)
        print("kartu komputer yang dibuka ",module.membukakartukom(komputer))
        print()
        tambahkartu=str(input("Apakah kamu ingin menambah kartu? ya/tidak: "))
        while (tambahkartu=="ya" or poinkomputer<=17):
            if tambahkartu=="ya":
                cekpemain=module.tambahkartu(kartu)
                jumlahkartuas=jumlahkartuas+module.mengecekkartuas(cekpemain)
                poinpemain=poinpemain+module.menghitungkartu(cekpemain)
                pemain.append(cekpemain)

                poinpemain=poinpemain-(10*kartuasbernilai11)
                kartuasbernilai11=0

                print("ini kartu kamu sekarang",pemain)
                cek=module.menghitungkartuas(jumlahkartuas)
                poinpemain=poinpemain+cek[0]
                kartuasbernilai11=cek[1]
                print("ini jumlah kartu kamu sekarang",poinpemain)

            if poinkomputer<=17:
                cekkomp=module.tambahkartu(kartu)
                poinkomputer=poinkomputer+module.menghitungkartu(cekkomp)
                komputer.append(cekkomp)

            if tambahkartu=="ya":
                tambahkartu=str(input("Apakah kamu ingin menambah kartu? ya/tidak: "))
                print("kartu komputer yang dibuka ",komputer)
            print("")

        chips=module.menghitunghasil(poinpemain,poinkomputer,chips,bet)
        module.updatechips(data[0],data[1],chips)
        komputer.append(komputer1)
        print(komputer,"Jumlah poin komputer: ",poinkomputer)
        print("")
        main=str(input("Apakah kamu ingin main? ya/tidak: "))
