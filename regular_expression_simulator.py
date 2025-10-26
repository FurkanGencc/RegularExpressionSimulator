# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 19:46:44 2025

@author: Turkuaz

FurkanGenç

"""
import random
    
print("Lütfen alfabeyi {} içine yazınız ve virgül ile ayırarak giriniz (örnek: {a,b,c})")
while True:
    alfabe = input("Alfabe: ")

    if alfabe[0] != "{" or alfabe[-1] != "}":
        print("Hatalı giriş! Alfabe {} içinde olmalı.")
        continue

    if alfabe[1] == ',' or alfabe[-2] == ',':
        print("Hatalı giriş! Başta veya sonda virgül olamaz.")
        continue

    i = 1  
    j = 2  
    hata_var = False
    son_virgul = False 

    while i < len(alfabe) - 1:
        ch = alfabe[i]

       
        if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
            print("Lütfen sadece harf kullanınız.")
            hata_var = True
            break

      
        if j < len(alfabe) - 1:
            if alfabe[j] != ',':
                print("Harflerden sonra virgül kullanın.")
                hata_var = True
                break

        i += 2
        j += 2

    if hata_var:
        continue  
    else:
        print("Alfabe başarıyla alındı:", alfabe)
        break


alfabe_list=[]
for i in alfabe:
    if i.isalpha():
        alfabe_list.append(i)
        
        
print(alfabe_list)
print("\nDüzenli ifadeyi girerken yazdıgınız alfabenin elemanlarını yazınız ve yalnızca (),+,* elemanlarını kullanınız.\n")
j=0

while True:
    d_ifade=input("\nDüzenli ifade:")
    for i in d_ifade:
        if i not in alfabe_list and i not in '() *+':
            print("\nHatalı giriş.\n")
            print("Bu düzenli ifade girdiğiniz alfabeden üretilemez.\n")
            print("Düzenli ifadeyi girerken yazdıgınız alfabenin elemanlarını yazınız ve yalnızca (),+,* elemanlarını kullanınız.\n")
            break
    
    
    if i not in alfabe_list and i not in '()*+':
      continue
  
    if d_ifade[0] in '*+' or d_ifade[-1] in '+':
      print("Düzenli ifade '+' ifadeleri ile başlayıp bitemez ve '*' ile başlayamaz")
      continue
    for j in range(1, len(d_ifade)):
      if d_ifade[j]==d_ifade[j-1] and d_ifade[j] in '*+':
          print("Düzenli ifadede '**'  '++' gibi yan yana kullanmayınız ")
          break
    else:
        print("Düzenli ifade geçerli")
        break
     
   
    parantez=0
    i=0
    while i<len(d_ifade):
        ch=d_ifade[i]
        if ch=='(':
            parantez=parantez+1
        elif ch==')':
           if parantez==0:
            print("Parantez açılmamış")
            break
           parantez=parantez-1
        elif ch=='+':
             if parantez==0:
                 print("'+' operatörünü parantez içindeki seçimlerde kullanınız örnek(a+b) ")
                 break
        i+=1
    else:
        if parantez>0:
            print("Açılan parantezler kapanmamış")
            continue
        print("Düzenli ifade geçerli")
        break
   
  
while True:
    kelime_sayisi=input("Kaç kelime üretmek istiyorsunuz")
 
   
    if not kelime_sayisi.isdigit():
        print("Lütfen sayi giriniz")
        continue
    kelime_sayisi=int(kelime_sayisi)
    
    if int(kelime_sayisi)<=0:
       print("Lütfen sıfırdan büyük bir sayi giriniz")
       continue 
   
    break


for k in range(kelime_sayisi):
    çıktı = ''
    i = 0
    while i < len(d_ifade):
        harf = d_ifade[i]

        if harf == '(':
            par_son = i
            acik = 1
            while acik != 0:
                par_son += 1
                if d_ifade[par_son] == '(':
                    acik += 1
                elif d_ifade[par_son] == ')':
                    acik -= 1

            par_icerik = ''
            j = i + 1
            while j < par_son:
                h = d_ifade[j]
                if h in alfabe:
                    op = d_ifade[j+1] if j+1 < par_son else ''
                    if op == '*':
                        tekrar = random.randint(0,3)
                        par_icerik += h * tekrar
                        j += 2
                    else:
                        par_icerik += h
                        j += 1
                elif h == '+':
                    
                    secenek1 = par_icerik[-1] if par_icerik else ''
                    secenek2 = d_ifade[j+1] if j+1 < par_son else ''
                    secenekler = []
                    if secenek1:
                        secenekler.append(secenek1)
                    if secenek2:
                        secenekler.append(secenek2)
                    if secenekler:
                        secilen = random.choice(secenekler)
                        if secenek1:
                            par_icerik = par_icerik[:-1]  
                        par_icerik += secilen
                    j += 2
                else:
                    j += 1

          
            op2 = d_ifade[par_son+1] if par_son+1 < len(d_ifade) else ''
            if op2 == '*':
                tekrar = random.randint(0,3)
                çıktı += par_icerik * tekrar
                i = par_son + 2
            else:
                çıktı += par_icerik
                i = par_son + 1

        elif harf in alfabe:
            op = d_ifade[i+1] if i+1 < len(d_ifade) else ''
            if op == '*':
                tekrar = random.randint(0,3)
                çıktı += harf * tekrar
                i += 2
            else:
                çıktı += harf
                i += 1
        else:
            i += 1

    print(çıktı)
