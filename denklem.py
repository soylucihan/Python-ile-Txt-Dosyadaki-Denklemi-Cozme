#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def dosyadan_oku(dosya_adi):
    ad=str(dosya_adi)
    dosya = open(ad,"r")
    dizi = dosya.readlines()
    ydizi=list()
    for a in dizi:
       
        ydizi.append(a.rstrip("\n"))
    return ydizi


def hesapla(a,b,c,x):
    return a*x*x + b*x + c

def satir_ortalama(x):
    toplam=0
    for i in x:
        toplam+=int(i)
    return toplam/len(x)


dosyaadi=input("dosya adini girin: ")
xler=dosyadan_oku(dosyaadi)

sonuclar=list()
print("a*x2 + b*x + c  polinomu icin ")
while True:
    try:
        a=int(input("a degeri girin: "))
        break
    except:
        print("sadece sayi girebilirsiniz")
while True:
    try:
        b=int(input("b degeri girin: "))
        break
    except:
        print("sadece sayi girebilirsiniz")
while True:
    try:
        c=int(input("c degeri girin: "))
        break
    except:
        print("sadece sayi girebilirsiniz")
        

for k in xler:
    sonuclar.append(hesapla(a,b,c,int(k)))
    
#print(xler)
#print(sonuclar)
print("ortalama= {} ".format(satir_ortalama(xler)))




plt.plot(xler,sonuclar )

plt.title("{0}*x^2 + {1}*x + {2} Grafigi".format(a,b,c))
plt.xlabel("x Degerleri")
plt.ylabel("Polinomun Degeri")
plt.show()
