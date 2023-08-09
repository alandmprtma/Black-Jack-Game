from gettext import install
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
magenta = fg('magenta_3a')

red = fg('red_3a')
green = fg('green_1')
gold = fg('light_goldenrod_3')
black = fg('black')


def membuatkartu():
    kartu=[]
    for i in range (1,5):
        for j in range (1,14):
            if i==1 and j<=10:
                temp=str(j)
                temp=temp+"Hearts"
                kartu.append(temp)
            elif i==1 and j==11:
                temp="Jack of Hearts"
                kartu.append(temp)
            elif i==1 and j==12:
                temp="Queen of Hearts"
                kartu.append(temp)
            elif i==1 and j==13:
                temp="king of Hearts"
                kartu.append(temp)
            elif i==2 and j<=10:
                temp=str(j)
                temp=temp+"Spade"
                kartu.append(temp)
            elif i==2 and j==11:
                temp="Jack of Spade"
                kartu.append(temp)
            elif i==2 and j==12:
                temp="Queen of Spade"
                kartu.append(temp)
            elif i==2 and j==13:
                temp="King of Spade"
                kartu.append(temp)
            elif i==3 and j<=10:
                temp=str(j)
                temp=temp+"Clubs"
                kartu.append(temp)
            elif i==3 and j==11:
                temp="Jack of Clubs"
                kartu.append(temp)
            elif i==3 and j==12:
                temp="Queen of Clubs"
                kartu.append(temp)
            elif i==3 and j==13:
                temp="King of Clubs"
                kartu.append(temp)
            elif i==4 and j<=10:
                temp=str(j)
                temp=temp+"Diamond"
                kartu.append(temp)
            elif i==4 and j==11:
                temp="Jack of Diamond"
                kartu.append(temp)
            elif i==4 and j==12:
                temp="Queen of Diamond"
                kartu.append(temp)
            elif i==4 and j==13:
                temp="King of Diamond"
                kartu.append(temp)
    return kartu

def membagikartu(card):
    temp=random.choice(card)
    card.remove(temp)
    return temp

def mengecekkartuas(player):
    if player[0]=='1' and player[1]!='0':
        return 1
    else:
        return 0

def menghitungkartu(player):
    if player[0]=='J' or player[0]=='Q' or player[0]=='K' or player[1]=='0':
        return 10
    else:
        return int(player[0])

def menghitungkartuas(sum_as):
    temppoinpemain=0
    tempkartuasbernilai11=0
    for i in range(0,sum_as):
        temp=int(input(f"masukkan nilai yang anda inginkan antara 1/11 untuk kartu as ke{i+1} "))
        if temp==11:
            temppoinpemain=temppoinpemain+10
            tempkartuasbernilai11=tempkartuasbernilai11+1
    tempp=[int(temppoinpemain),int(tempkartuasbernilai11)]
    return tempp
    
def membukakartukom(comp):
    compp=comp
    compp.remove(compp[0])
    return compp

def tambahkartu(card):
    kartutambah=random.choice(card)
    card.remove(kartutambah)
    return kartutambah

def menghitunghasil(player,comp,chips,bet):
    selisih1=abs(21-player)
    selisih2=abs(21-comp)
    chips=int(chips)
    bet=int(bet)
    if player>21 and comp<=21:
        print(red + "kamu kalah")
        chips -= bet
        print("Chips kamu sekarang: ", chips)
    elif comp>21 and player<=21:
        print(green+"kamu menang")
        chips += bet * 2
        print("Chips kamu sekarang: ",chips)
    elif selisih1<selisih2:
        print(green+ "kamu menang")
        chips += bet * 2
        print("Chips kamu sekarang: ",chips)
    elif selisih1>selisih2:
        print(red + "kamu kalah")
        chips -= bet
        print("Chips kamu sekarang: ",chips)
    else:
        print(black + "seri")
        print("Chips kamu sekarang: ",chips)
    return chips

def fungsimenu():
    Prioritas_pemenang = ( blue1 +"Prioritas pemenang: ")
    Prioritas_Pemenang1 = (blue2 + "Prioritas pemenang pertama adalah total nilai angka pada kartu sama dengan 21. |")
    Prioritas_Pemenang2 = (blue3 +"Prioritas pemenang kedua adalah total nilai angka pada kartu kurang dari 21, tetapi selisihnya dengan 21 paling kecil dibandingkan lawan. |")
    Prioritas_Pemenang3 = (blue4 +"Prioritas pemenang ketiga adalah total nilai angka pada kartu lebih dari 21, tetapi selisihnya dengan 21 paling kecil dibandingkan lawan. |")
    Langkah_Bermain = ("Cara Bermain: ")
    Langkah_Bermain1 = (blue1 +"1. Kartu akan dibagikan secara random dengan kartu pertama hanya dapat dilihat oleh pemain. |")
    Langkah_Bermain2 = (blue2 +"2. Pemain dapat memilih 'ya' apabila ingin terus menambah kartu. |")
    Langkah_Bermain3 = (blue3 +"3. Jika pemain sudah memilih untuk tidak menambah kartu, penghitungan total nilai kartu akan dijalankan. |")
    Langkah_Bermain4 = (blue4 +"4. Pemenang ditentukan berdasarkan jumlah nilai angka kartu sesuai prioritas. |")

    print(deep_pink_4c + "1. Main!")
    print()
    print(medium_violet_red +"2. Lihat Cara Bermain!")
    print()
    print(darkviolet + "3. Kembali ke lobby")
    Menu = str(input("1/2/3 = "))
    if Menu == "1":
        main=str(input("Apakah kamu ingin main?(ya/tidak): "))
    elif Menu == "2" :
        print()
        print(Prioritas_pemenang)
        print(Prioritas_Pemenang1)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Prioritas_Pemenang2) 
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Prioritas_Pemenang3)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print()
        print(Langkah_Bermain)
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Langkah_Bermain1) 
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Langkah_Bermain2) 
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Langkah_Bermain3) 
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(Langkah_Bermain4)

        print( )
        main=str(input("Apakah kamu ingin main?(ya/tidak): "))
    
    else :
        begin()
    return main
def login(name,password):
    sukses = False
    file = open("Tubes/login.txt",'r')
    for i in file:
        data = i.split(",")
        a = data[0]
        b = data[1]
        saldo = data[2]
        if(a==name and b == password):
            sukses = True
            break
    if sukses == True:
        print("login berhasil, silahkan masuk")
        print(f"Saldo anda saat ini adalah {saldo}")
        return saldo
    else:
        print()
        print()
        print("anda belum terdaftar, silahkan register")
        print()
    file.close()
    begin()


def register():
    print("Masukkan ID dan password anda yang baru")
    name = input("Masukkan ID :")
    password = input("Masukkan Password :")
    saldo = input("Masukkan Saldo: ")
    with open("Tubes/login.txt", mode="a") as file:
        file.write(f"{name},{password},{saldo}\n")
    print()
    print("register anda berhasil, silahkan masuk")
    file.close()
    begin()


def access(option):
    if (option == "login"):
        name = input("masukkan ID : ")
        password = input("masukkan Password : ")
        chips=login(name,password)
        data=[name,password,chips]
        return data
    else:
        register()
        return 'login'

def begin():
    global option 

    print()
    print()
    print()
    print(purple +' ♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦||SELAMAT DATANG DI PERMAINAN||♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦  ♣♠♥♦')
    print(darkviolet +'♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦')
    print(magenta +'♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠♥♦    ♣♠♥♦    ♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠♥♦    ♣♠♥♦    ♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠')
    print(medium_violet_red + '♥♦ ♣♠  ♥♦ ♣♠  ♥♦ ♥♦ ♣♠  ♥♦ ♣♠  ♥♦ ♥♦ ♣♠  ♥♦ ♣♠  ♥♦ ♥♦ ♣♠  ♥♦ ♣♠  ♥♦ ♥♦ ♣♠  ♥♦ ♣♠  ♥♦ ♥♦ ♣♠  ♥♦ ♥♦ ♣♠')
    print(deep_pink_4c +' ♥  ♣    ♠    ♥    ♦    ♣    ♠    ♥    ♦    ♣    ♠    ♥    ♦    ♣    ♠    ♣    ♠    ♥    ♦    ♣    ♠   ')
    v = pyfiglet.figlet_format(' Blackjack', font='roman', width = 100)
    print(deep_pink_4c + v)
    print(deep_pink_4c +" ♣♠♥♦  ♣♠♥♦  ♣♠♥♦ |||Ketik 'login' jika anda sudah punya akun permainan Blackjack||| ♣♠♥♦  ♣♠♥♦  ♣♠♥♦ ")
    print(medium_violet_red +" ♥♦ ♣♠  ♥♦ ♣♠  ♥♦||Ketik 'register' jika anda belum punya akun permainan Blackjack||♣♠  ♥♦ ♣♠  ♥♦ ♣♠")
    print(magenta +'♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦    ♣♠♥♦')
    print(darkviolet +'♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠♥♦    ♣♠♥♦    ♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠♥♦    ♣♠♥♦    ♣♠♥  ♦    ♣♠  ♥♦    ♣  ♠')
    print(purple +' ♥  ♣    ♠    ♥    ♦    ♣    ♠    ♥    ♦    ♣    ♠    ♥    ♦    ♣    ♠    ♣    ♠    ♥    ♦    ♣    ♠   ')   
    print()
    print()
    
    option = input("silahkan masukkan (login/register) :")
    if option != "login" and option != "register":
        begin()
    else:
        return option
        
def updatechips(name,password,chips):
    tempp=0
    with open("Tubes/login.txt",mode="r") as file:
        for i in file:
            data = i.split(",")
            a = data[0]
            b = data[1]
            tempp=tempp+1
            if(a==name and b == password):
                data[2]=(f"{chips}\n")
                break
        file.seek(0)
        temp=file.readlines()
    temp[tempp-1]=",".join(data)
    with open("Tubes/login.txt",mode="w") as files:
        files.writelines(temp)
