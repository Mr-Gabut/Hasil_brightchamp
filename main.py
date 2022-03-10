# Program tebak angka
import os,sys,time,random

angka_random = int(input("[+] Masukan angka : "))
kamis = random.randint(1,5)

while angka_random != "kamis":
  if angka_random > kamis:
    print ("Ups angka kamu kegedean\n Belum mandi ya?!!!")
    angka_random = int(input("[+] Masukan angka : "))
  elif angka_random < kamis:
    print ("Upss angka kamu kekecilan\n Belum shollat makannya kecil angkanya... hihi")
    angka_random = int(input("[+] Masukan angka : "))
  else : 
    print ("Selamat angka kamu teppat \n Semoga cepet nikkah ya kak... hihi")
    
    break
